from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def init_data():
    try:
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w') as f:
                json.dump({}, f)
    except:
        pass

init_data()

@app.route('/data', methods=['GET'])
def get_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data}), 200
    except:
        return jsonify({"success": False, "error": "Failed to retrieve data"}), 500

@app.route('/data', methods=['POST'])
def post_data():
    try:
        body = request.get_json()
        if not body:
            return jsonify({"success": False, "error": "No data provided"}), 400
        with open(DATA_FILE, 'w') as f:
            json.dump(body, f, indent=2)
        return jsonify({"success": True, "message": "Data saved successfully", "data": body}), 201
    except:
        return jsonify({"success": False, "error": "Failed to save data"}), 500

@app.route('/data', methods=['PATCH'])
def patch_data():
    try:
        updates = request.get_json()
        if not updates:
            return jsonify({"success": False, "error": "No update data provided"}), 400
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        data.update(updates)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        return jsonify({"success": True, "message": "Data updated successfully", "data": data}), 200
    except:
        return jsonify({"success": False, "error": "Failed to update data"}), 500

@app.route('/data', methods=['DELETE'])
def delete_data():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
        return jsonify({"success": True, "message": "Data deleted successfully"}), 200
    except:
        return jsonify({"success": False, "error": "Failed to delete data"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
