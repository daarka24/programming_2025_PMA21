from user import User
from flask import Flask, request, jsonify
import  json, os

app = Flask(__name__)

FILE = "data.json"

def write_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

def read_from_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

@app.route("/user", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        user = User.from_dict(data)
        write_to_file(FILE, user.to_dict())
        return jsonify({"message": "User added"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/user", methods=["GET"])
def get_user():
    if not os.path.exists(FILE):
        return jsonify({"message": "There are no data"}), 404
    try:
        data = read_from_file(FILE)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/user", methods=["DELETE"])
def delete_user():
    if not os.path.exists(FILE):
        return jsonify({"message": "There are no data to delete"}), 404
    else:
        os.remove(FILE)
        return jsonify({"message": "User deleted"}), 200

@app.route("/user", methods=["PATCH"])
def update_user():
    if not os.path.exists(FILE):
        return jsonify({"message": "There are no data to update"}), 404
    try:
        to_update = request.get_json()
        data = read_from_file(FILE)
        for key in to_update:
            if key in data:
                data[key] = to_update[key]
        write_to_file(FILE, data)
        return jsonify({"message": "User updated"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=555, debug=True)