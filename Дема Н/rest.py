from flask import Flask, request, jsonify
import os
import json
from cartoon import Cartoon
app = Flask(__name__)
file = ("data.json")

def read():
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            return []
def save(data):
    with open(file, "w") as f:
        return f.write(json.dumps(data))
@app.route("/data", methods=["POST"])
def create():
    raw_data = request.get_json()
    cartoon_obj, error = Cartoon.input(raw_data)
    if error:
        return jsonify({"error": error}), 400
    try:
        current_data = read()
        for item in current_data:
            if item["name"] == cartoon_obj.name:
                return jsonify({"error": "name already exists"}), 400
        current_data.append(cartoon_obj.to_dict())
        save(current_data)
        return jsonify({"data": current_data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route("/data", methods=["GET"])
def get():
    if not os.path.exists(file):
        return jsonify({"status": "error"}), 404
    with (open(file, "r") as f):
        try:
            data = read()
            return jsonify({"data": data}), 200
        except Exception as e:
            return jsonify({"status": "error"}), 500
@app.route("/data/<name>", methods=["PATCH"])
def update(name):
    updates = request.get_json()
    if not updates:
        return jsonify({"status": "error"}), 400
    current_data = read()
    found = False
    try:
        for item in current_data:
            if item["name"] == name:
                if "year" in updates:
                    item["year"] = updates["year"]
                if "genre" in updates:
                    item["genre"] = updates["genre"]
                if "name" in updates:
                    item["name"] = updates["name"]
                found = True
                break
        if not found:
            return jsonify({"status": "error"}), 404
        save(current_data)
        return jsonify({"status": "updated", "data": item}), 200
    except Exception as e:
        return jsonify({"status": "error"}), 500
@app.route("/data/<name>", methods =["DELETE"])
def delete(name):
    current_data = read()
    new_data = [item for item in current_data if item["name"] != name]
    if len(new_data) == len(current_data):
        return jsonify({"status": "error"}), 404
    try:
        save(new_data)
        return jsonify({"status": "deleted", "name": name}), 200
    except Exception as e:
        return jsonify({"status": "error"}), 500
if __name__ == "__main__":
    app.run(debug=True, port=5004)