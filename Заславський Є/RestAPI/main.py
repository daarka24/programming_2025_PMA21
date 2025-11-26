from flask import Flask, request, jsonify
from person import Person
import json
import os

app = Flask(__name__)
FILE_NAME = "data.json"


def save_to_file(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_from_file():
    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, encoding="utf-8") as f:
        return json.load(f)


@app.route("/person", methods=["POST"])
def create_person():
    try:
        body = request.get_json()

        person = Person.from_dict(body)

        save_to_file(person.to_dict())
        return jsonify({"message": "Saved"}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Server error"}), 500


@app.route("/person", methods=["GET"])
def get_person():
    try:
        data = load_from_file()

        if not data:
            return jsonify({"error": "No data"}), 404

        return jsonify(data), 200

    except Exception:
        return jsonify({"error": "Server error"}), 500


@app.route("/person", methods=["PATCH"])
def update_person():
    try:
        data = load_from_file()

        if not data:
            return jsonify({"error": "No data to update"}), 404

        updates = request.get_json()

        for key in updates:
            if key in data:
                data[key] = updates[key]

        save_to_file(data)

        return jsonify({"message": "Updated"}), 200

    except Exception:
        return jsonify({"error": "Server error"}), 500


@app.route("/person", methods=["DELETE"])
def delete_person():
    try:

        if not os.path.exists(FILE_NAME):
            return jsonify({"error": "No data to delete"}), 404

        os.remove(FILE_NAME)

        return jsonify({"message": "Deleted"}), 200

    except Exception:
        return jsonify({"error": "Server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
