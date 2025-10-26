from flask import Flask, request, jsonify
import sqlite3
import threading

app = Flask(__name__)
DB_NAME = 'persons.db'
db_lock = threading.Lock()


def init_db():
    with db_lock:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT,
                age INTEGER
            )
        ''')
        conn.commit()
        conn.close()


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api/persons', methods=['POST'])
def create_person():
    try:
        data = request.get_json()

        if not data or 'full_name' not in data:
            return jsonify({'error': 'full_name is required'}), 400

        with db_lock:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO persons (full_name, email, age) VALUES (?, ?, ?)',
                (data['full_name'], data.get('email'), data.get('age'))
            )
            conn.commit()
            person_id = cursor.lastrowid
            conn.close()

        return jsonify({
            'id': person_id,
            'full_name': data['full_name'],
            'email': data.get('email'),
            'age': data.get('age'),
            'message': 'Person created successfully'
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM persons WHERE id = ?', (person_id,))
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return jsonify({'error': 'Person not found'}), 404

        return jsonify({
            'id': row['id'],
            'full_name': row['full_name'],
            'email': row['email'],
            'age': row['age']
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons', methods=['GET'])
def get_all_persons():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM persons')
        rows = cursor.fetchall()
        conn.close()

        persons = []
        for row in rows:
            persons.append({
                'id': row['id'],
                'full_name': row['full_name'],
                'email': row['email'],
                'age': row['age']
            })

        return jsonify(persons), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>', methods=['PATCH'])
def update_person(person_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        with db_lock:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if person exists
            cursor.execute('SELECT * FROM persons WHERE id = ?', (person_id,))
            if cursor.fetchone() is None:
                conn.close()
                return jsonify({'error': 'Person not found'}), 404

            # Build update query dynamically
            update_fields = []
            values = []

            if 'full_name' in data:
                update_fields.append('full_name = ?')
                values.append(data['full_name'])
            if 'email' in data:
                update_fields.append('email = ?')
                values.append(data['email'])
            if 'age' in data:
                update_fields.append('age = ?')
                values.append(data['age'])

            if not update_fields:
                conn.close()
                return jsonify({'error': 'No valid fields to update'}), 400

            values.append(person_id)
            query = f"UPDATE persons SET {', '.join(update_fields)} WHERE id = ?"

            cursor.execute(query, values)
            conn.commit()

            # Get updated person
            cursor.execute('SELECT * FROM persons WHERE id = ?', (person_id,))
            row = cursor.fetchone()
            conn.close()

        return jsonify({
            'id': row['id'],
            'full_name': row['full_name'],
            'email': row['email'],
            'age': row['age'],
            'message': 'Person updated successfully'
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        with db_lock:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if person exists
            cursor.execute('SELECT * FROM persons WHERE id = ?', (person_id,))
            if cursor.fetchone() is None:
                conn.close()
                return jsonify({'error': 'Person not found'}), 404

            cursor.execute('DELETE FROM persons WHERE id = ?', (person_id,))
            conn.commit()
            conn.close()

        return jsonify({'message': 'Person deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    init_db()
    print("Server 2 (Database Server) starting on http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)
