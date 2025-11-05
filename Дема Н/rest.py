from flask import Flask, request, jsonify
import os
import json
app = Flask(__name__)
file = ("data.json")

@app.route("/data", methods=["POST"])
def create():
    data = request.get_json()
    if not isinstance(data, list):
        data = [data]
    with open(file, "w") as f:
        json.dump(data, f)
    return jsonify({"status": "ok", "data": data})
@app.route("/data", methods=["GET"])
def get():
    if not os.path.exists(file):
        return jsonify({"status": "error"}), 404
    with open(file, "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = []
    return jsonify(data), 200
@app.route("/data/<id>", methods=["PATCH"])
def put(id):
    if not os.path.exists(file):
        return jsonify({"error": "Not work"}), 404
    with open(file, "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            return jsonify({"error": "Not work"}), 500
    updated = request.get_json()
    found = False
    for item in data:
        if str(item.get("id")) == str(id):
            item.update(updated)
            found = True
            break
    if not found:
        return jsonify({"error": "Not found"}), 404
    with open(file, "w") as f:
        json.dump(data, f, ensure_ascii=False)
    return jsonify({"status": "updated", "data": data}), 200
@app.route("/data", methods =["DELETE"])
def delete():
    with open(file, "w") as f:
        json.dump([], f)
    return jsonify({"status": "deleted"}), 200
if __name__ == "__main__":
    app.run(debug=True, port=5000)