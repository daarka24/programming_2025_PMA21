from flask import Flask, request, jsonify
import psycopg2
import pika
import json
import redis
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "people_db"),
    "user": os.getenv("DB_USER", "user1"),
    "password": os.getenv("DB_PASS", "pass1"),
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", 5432))
}
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "127.0.0.1")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "data_processing_queue")
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
SERVER_DB_PORT = int(os.getenv("SERVER_DB_PORT", 6000))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)


def get_conn():
    return psycopg2.connect(**DB_CONFIG)


def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def send_to_queue(message_data):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
        channel.basic_publish(
            exchange='',
            routing_key=RABBITMQ_QUEUE,
            body=json.dumps(message_data, ensure_ascii=False),
            properties=pika.BasicProperties(delivery_mode=2, content_type='application/json')
        )
        connection.close()
        return True
    except Exception as e:
        print(f"MQ Error: {e}")
        return False


def invalidate_cache(person_id):
    try:
        r.delete(f"person:{person_id}")
    except Exception:
        pass


@app.route("/save", methods=["POST"])
def create_person():
    data = request.get_json()
    if not data:
        return jsonify({"error": "no json body"}), 400

    if not all(k in data for k in ["name", "surname", "birth_date"]):
        return jsonify({"error": "missing fields"}), 400

    if not validate_date(data["birth_date"]):
        return jsonify({"error": "invalid date format"}), 400

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO people (name, surname, birth_date) VALUES (%s, %s, %s) RETURNING id",
            (data["name"], data["surname"], data["birth_date"])
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        response_data = {
            "operation": "created",
            "id": new_id,
            "name": data["name"],
            "surname": data["surname"],
            "birth_date": data["birth_date"],
            "saved_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        send_to_queue(response_data)
        return jsonify(response_data), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get/<int:person_id>", methods=["GET"])
def get_person(person_id):
    cache_key = f"person:{person_id}"
    try:
        cached = r.get(cache_key)
        if cached:
            return jsonify({"data": json.loads(cached), "source": "redis"}), 200
    except Exception:
        pass

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, name, surname, birth_date FROM people WHERE id = %s", (person_id,))
        record = cur.fetchone()
        cur.close()
        conn.close()

        if not record:
            return jsonify({"error": "not found"}), 404

        db_data = {
            "id": record[0],
            "name": record[1],
            "surname": record[2],
            "birth_date": record[3].strftime('%Y-%m-%d')
        }

        try:
            r.setex(cache_key, 60, json.dumps(db_data))
        except Exception:
            pass

        return jsonify({"data": db_data, "source": "postgresql"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/person/<int:person_id>", methods=["PATCH", "DELETE"])
def handle_person_update(person_id):
    if request.method == "PATCH":
        data = request.get_json()
        if not data:
            return jsonify({"error": "no json body"}), 400

        updates = {k: v for k, v in data.items() if k in ["name", "surname", "birth_date"]}
        if not updates:
            return jsonify({"error": "no valid fields"}), 400

        if "birth_date" in updates and not validate_date(updates["birth_date"]):
            return jsonify({"error": "invalid date"}), 400

        try:
            set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
            values = list(updates.values())
            values.append(person_id)

            conn = get_conn()
            cur = conn.cursor()
            query = f"UPDATE people SET {set_clause} WHERE id = %s RETURNING id, name, surname, birth_date"
            cur.execute(query, tuple(values))
            updated_record = cur.fetchone()
            conn.commit()
            cur.close()
            conn.close()

            if not updated_record:
                return jsonify({"error": "not found"}), 404

            invalidate_cache(person_id)

            response_data = {
                "operation": "updated",
                "id": updated_record[0],
                "name": updated_record[1],
                "surname": updated_record[2],
                "birth_date": updated_record[3].strftime('%Y-%m-%d')
            }
            send_to_queue(response_data)
            return jsonify(response_data), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == "DELETE":
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("DELETE FROM people WHERE id = %s RETURNING id", (person_id,))
            deleted_id = cur.fetchone()
            conn.commit()
            cur.close()
            conn.close()

            if not deleted_id:
                return jsonify({"error": "not found"}), 404

            invalidate_cache(person_id)

            send_to_queue({"operation": "delete", "id": person_id})
            return jsonify({"status": "deleted", "id": person_id}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=SERVER_DB_PORT, debug=True)