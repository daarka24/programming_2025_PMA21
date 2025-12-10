from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SERVER_DB_HOST = os.getenv("SERVER_DB_HOST", "127.0.0.1")
SERVER_DB_PORT = int(os.getenv("SERVER_DB_PORT", 6000))
PROXY_PORT = int(os.getenv("PROXY_PORT", 5000))

BASE_URL = f"http://{SERVER_DB_HOST}:{SERVER_DB_PORT}"

@app.route("/receive", methods=["POST"])
def proxy_create():
    try:
        resp = requests.post(f"{BASE_URL}/save", json=request.get_json())
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 502

@app.route("/get/<int:person_id>", methods=["GET"])
def proxy_read(person_id):
    try:
        resp = requests.get(f"{BASE_URL}/get/{person_id}")
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 502

@app.route("/person/<int:person_id>", methods=["PATCH", "DELETE"])
def proxy_update_delete(person_id):
    url = f"{BASE_URL}/person/{person_id}"
    try:
        if request.method == "PATCH":
            resp = requests.patch(url, json=request.get_json())
        elif request.method == "DELETE":
            resp = requests.delete(url)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PROXY_PORT, debug=True)