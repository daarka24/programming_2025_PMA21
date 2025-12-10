import pika
import json
import requests
import time
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "127.0.0.1")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "data_processing_queue")
PROCESSOR_HOST = os.getenv("PROCESSOR_HOST", "127.0.0.1")
PROCESSOR_PORT = int(os.getenv("PROCESSOR_PORT", 8000))
DATA_PROCESSOR_URL = f"http://{PROCESSOR_HOST}:{PROCESSOR_PORT}/enhance"
MONGO_HOST = os.getenv("MONGO_HOST", "127.0.0.1")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "processing_db")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "processed_data")

try:
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT, serverSelectionTimeoutMS=5000)
    db = client[MONGO_DB_NAME]
    collection = db[MONGO_COLLECTION_NAME]
    client.server_info()
    print(f"Connected to MongoDB: {MONGO_HOST}:{MONGO_PORT}")
except Exception as e:
    print(f"FATAL ERROR: Could not connect to MongoDB: {e}")
    exit(1)


def callback(ch, method, properties, body):
    try:
        print(f"\n{'=' * 70}")
        print(f"[RECEIVED] MESSAGE FROM QUEUE")
        print(f"{'=' * 70}")
        message = json.loads(body)

        operation = message.get("operation")
        person_id = message.get("id")

        if not operation or not person_id:
            print(f"[ERROR] Invalid message format. 'operation' or 'id' missing.")
            print(f"    Message body: {body.decode()}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            return

        print(f"Operation: {operation.upper()}, Person ID: {person_id}")

        if operation in ["created", "updated"]:
            print(f"\n[→] Sending to data_processor ({DATA_PROCESSOR_URL})...")
            response = requests.post(DATA_PROCESSOR_URL, json=message, timeout=10)

            if response.status_code == 200:
                enhanced_data = response.json()
                print(f"\n[PROCESSED] BY SECOND SERVER:")
                print(f"   Status: {enhanced_data.get('processing_status', '')}")

                print(f"\n[→] Upserting processed data to MongoDB...")
                try:
                    result = collection.update_one(
                        {"id": person_id},
                        {"$set": enhanced_data},
                        upsert=True
                    )

                    print(f"[SAVE] Data saved to MongoDB (Operation: {operation})")
                    if result.upserted_id:
                        print(f"    Action: CREATED new document (Mongo ID: {result.upserted_id})")
                    elif result.modified_count > 0:
                        print(f"    Action: UPDATED existing document.")
                    else:
                        print(f"    Action: No changes needed in MongoDB.")

                    ch.basic_ack(delivery_tag=method.delivery_tag)
                    print(f"\n[✓] Message for '{operation}' processed and removed from queue.")

                except Exception as e:
                    print(f"\n[ERROR] MongoDB save error: {str(e)}")
                    ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

            else:
                print(f"\n[ERROR] Processing error: {response.status_code}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

        elif operation == "delete":
            print(f"\n[→] Deleting processed data from MongoDB...")
            try:
                result = collection.delete_one({"id": person_id})

                if result.deleted_count > 0:
                    print(f"[SAVE] Document for person_id {person_id} deleted from MongoDB.")
                else:
                    print(f"[INFO] Document for person_id {person_id} not found in MongoDB (already deleted).")

                ch.basic_ack(delivery_tag=method.delivery_tag)
                print(f"\n[✓] Message for 'delete' processed and removed from queue.")

            except Exception as e:
                print(f"\n[ERROR] MongoDB delete error: {str(e)}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

        else:
            print(f"[ERROR] Unknown operation: '{operation}'")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Connection error with data_processor: {str(e)}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
    except Exception as e:
        print(f"\n[ERROR] General processing error: {str(e)}")
        print(f"    Message body: {body.decode()}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


def main():
    while True:
        try:
            print("\n" + "=" * 70)
            print("CONSUMER - RABBITMQ → MONGODB (CRUD enabled)")
            print("=" * 70)
            print(f"RabbitMQ:      {RABBITMQ_HOST} (Queue: {RABBITMQ_QUEUE})")
            print(f"Processor:     {DATA_PROCESSOR_URL}")
            print(f"Database:      MongoDB at {MONGO_HOST}:{MONGO_PORT}")
            print("=" * 70)
            print("Waiting for messages... (Ctrl+C to exit)\n")

            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=False)
            channel.start_consuming()
        except KeyboardInterrupt:
            print("\n\n" + "=" * 70);
            print("[!] CONSUMER STOPPED");
            print("=" * 70);
            break
        except pika.exceptions.AMQPConnectionError:
            print(f"\n[ERROR] Could not connect to RabbitMQ on {RABBITMQ_HOST}")
            print(f"[RETRY] Reconnecting in 5 seconds...\n");
            time.sleep(5)
        except Exception as e:
            print(f"\n[ERROR] {str(e)}");
            print(f"[RETRY] Reconnecting in 5 seconds...\n");
            time.sleep(5)


if __name__ == "__main__":
    main()