from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'


def read_data():
    if not os.path.exists(DATA_FILE):
        return None
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return None



def write_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



@app.route('/object', methods=['POST'])
def create_object():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Body is missing"}), 400

        write_data(data)
        return jsonify({"message": "Object saved successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/object', methods=['GET'])
def get_object():
    try:
        data = read_data()
        if not data:
            return jsonify({"error": "Object not found"}), 404
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/object', methods=['PATCH'])
def update_object():
    try:
        new_data = request.get_json()
        if not new_data:
            return jsonify({"error": "Body is missing"}), 400

        current_data = read_data()
        if not current_data:
            return jsonify({"error": "Object not found"}), 404

        current_data.update(new_data)
        write_data(current_data)
        return jsonify({"message": "Object updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/object', methods=['DELETE'])
def delete_object():
    try:
        if not os.path.exists(DATA_FILE):
            return jsonify({"error": "Object not found"}), 404

        os.remove(DATA_FILE)
        return jsonify({"message": "Object deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)
