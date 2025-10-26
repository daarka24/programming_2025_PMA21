from flask import Flask, request, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
SERVER2_URL = 'http://localhost:5001'
executor = ThreadPoolExecutor(max_workers=10)


def combine_name(first_name, last_name):
    return f"{first_name} {last_name}".strip()


def forward_to_server2(method, endpoint, data=None):
    url = f"{SERVER2_URL}{endpoint}"

    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    elif method == 'PATCH':
        response = requests.patch(url, json=data)
    elif method == 'DELETE':
        response = requests.delete(url)
    else:
        raise ValueError(f"Unsupported method: {method}")

    return response


@app.route('/api/persons', methods=['POST'])
def create_person_blocking():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        if 'first_name' not in data or 'last_name' not in data:
            return jsonify({'error': 'first_name and last_name are required'}), 400

        full_name = combine_name(data['first_name'], data['last_name'])

        server2_data = {
            'full_name': full_name,
            'email': data.get('email'),
            'age': data.get('age')
        }

        response = forward_to_server2('POST', '/api/persons', server2_data)

        return jsonify(response.json()), response.status_code

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to database server'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/async', methods=['POST'])
def create_person_nonblocking():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        if 'first_name' not in data or 'last_name' not in data:
            return jsonify({'error': 'first_name and last_name are required'}), 400

        full_name = combine_name(data['first_name'], data['last_name'])

        server2_data = {
            'full_name': full_name,
            'email': data.get('email'),
            'age': data.get('age')
        }

        future = executor.submit(forward_to_server2, 'POST', '/api/persons', server2_data)

        return jsonify({
            'message': 'Request submitted for processing',
            'status': 'pending'
        }), 202

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>', methods=['GET'])
def get_person_blocking(person_id):
    try:
        response = forward_to_server2('GET', f'/api/persons/{person_id}')
        return jsonify(response.json()), response.status_code

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to database server'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons', methods=['GET'])
def get_all_persons_blocking():
    try:
        response = forward_to_server2('GET', '/api/persons')
        return jsonify(response.json()), response.status_code

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to database server'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>', methods=['PATCH'])
def update_person_blocking(person_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        server2_data = {}

        if 'first_name' in data or 'last_name' in data:
            current_response = forward_to_server2('GET', f'/api/persons/{person_id}')
            if current_response.status_code == 200:
                current_data = current_response.json()
                current_full_name = current_data.get('full_name', '')

                parts = current_full_name.split(' ', 1)
                current_first = parts[0] if len(parts) > 0 else ''
                current_last = parts[1] if len(parts) > 1 else ''

                first_name = data.get('first_name', current_first)
                last_name = data.get('last_name', current_last)

                server2_data['full_name'] = combine_name(first_name, last_name)

        if 'email' in data:
            server2_data['email'] = data['email']
        if 'age' in data:
            server2_data['age'] = data['age']

        response = forward_to_server2('PATCH', f'/api/persons/{person_id}', server2_data)

        return jsonify(response.json()), response.status_code

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to database server'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>/async', methods=['PATCH'])
def update_person_nonblocking(person_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        server2_data = {}

        if 'first_name' in data or 'last_name' in data:
            current_response = forward_to_server2('GET', f'/api/persons/{person_id}')
            if current_response.status_code == 200:
                current_data = current_response.json()
                current_full_name = current_data.get('full_name', '')

                parts = current_full_name.split(' ', 1)
                current_first = parts[0] if len(parts) > 0 else ''
                current_last = parts[1] if len(parts) > 1 else ''

                first_name = data.get('first_name', current_first)
                last_name = data.get('last_name', current_last)

                server2_data['full_name'] = combine_name(first_name, last_name)

        if 'email' in data:
            server2_data['email'] = data['email']
        if 'age' in data:
            server2_data['age'] = data['age']

        future = executor.submit(forward_to_server2, 'PATCH', f'/api/persons/{person_id}', server2_data)

        return jsonify({
            'message': 'Update request submitted for processing',
            'status': 'pending'
        }), 202

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>', methods=['DELETE'])
def delete_person_blocking(person_id):
    try:
        response = forward_to_server2('DELETE', f'/api/persons/{person_id}')
        return jsonify(response.json()), response.status_code

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to database server'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/persons/<int:person_id>/async', methods=['DELETE'])
def delete_person_nonblocking(person_id):
    try:
        future = executor.submit(forward_to_server2, 'DELETE', f'/api/persons/{person_id}')

        return jsonify({
            'message': 'Delete request submitted for processing',
            'status': 'pending'
        }), 202

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index():
    return jsonify({
        'message': 'Server 1 - API Gateway',
        'endpoints': {
            'POST /api/persons': 'Create person (blocking)',
            'POST /api/persons/async': 'Create person (non-blocking)',
            'GET /api/persons': 'Get all persons (blocking)',
            'GET /api/persons/<id>': 'Get person by ID (blocking)',
            'PATCH /api/persons/<id>': 'Update person (blocking)',
            'PATCH /api/persons/<id>/async': 'Update person (non-blocking)',
            'DELETE /api/persons/<id>': 'Delete person (blocking)',
            'DELETE /api/persons/<id>/async': 'Delete person (non-blocking)'
        },
        'note': 'Use first_name and last_name in requests. They will be combined into full_name.'
    })


if __name__ == '__main__':
    print("Server 1 (API Gateway) starting on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

