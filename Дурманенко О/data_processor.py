from flask import Flask, request, jsonify
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

PROCESSOR_PORT = int(os.getenv("PROCESSOR_PORT", 8000))


@app.route("/enhance", methods=["POST"])
def enhance_data():
    data = request.get_json()
    if not data:
        print("Error: No JSON received")
        return jsonify({"error": "No JSON body provided"}), 400
    try:
        print(f"\n{'=' * 70}")
        print(f"DATA RECEIVED FROM CONSUMER:")
        print(f"{'=' * 70}")
        print(f"   Record ID:        {data.get('id', 'N/A')}")
        print(f"   Name:             {data.get('name', 'N/A')}")
        print(f"   Surname:          {data.get('surname', 'N/A')}")
        print(f"{'-' * 70}")

        enhanced_data = {
            **data,
            "additional_text": f"Processed by second server at {datetime.now().strftime('%H:%M:%S')}",
            "additional_info": f"Hello, {data.get('name', 'unknown')}! Your data has been successfully saved and processed.",
            "message": f"Record ID {data.get('id', '?')} created for {data.get('name', '')} {data.get('surname', '')}",
            "processing_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "processing_status": "Successfully processed by the second server",
            "processing_source": f"Second Server (port {PROCESSOR_PORT})",
            "route": "Client → Proxy → DB → RabbitMQ → Consumer → Second Server ✓",
            "additional_fields": {
                "name_length": len(data.get('name', '')),
                "surname_length": len(data.get('surname', '')),
                "formatted_name": f"{data.get('name', '')} {data.get('surname', '')}".strip(),
                "processed_at": datetime.now().isoformat()
            }
        }

        print(f"\nPROCESSING RESULT:")
        print(f"{'-' * 70}")
        print(f"   Message:          {enhanced_data.get('message')}")
        print(f"   Status:           {enhanced_data.get('processing_status')}")
        print(f"{'=' * 70}\n")

        return jsonify(enhanced_data), 200
    except Exception as e:
        print(f"\nPROCESSING ERROR: {str(e)}")
        return jsonify({"error": "Processing error on second server", "details": str(e), "original_data": data}), 500


@app.route("/health", methods=["GET"])
def health():
    health_status = {"status": "healthy", "server": "SECOND SERVER (DATA PROCESSOR)", "port": PROCESSOR_PORT,
                     "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    print(f"\nHealth Check - {health_status['timestamp']}")
    return jsonify(health_status), 200


@app.route("/", methods=["GET"])
def root():
    info = {"project": "SECOND SERVER (DATA PROCESSOR)", "port": PROCESSOR_PORT,
            "version": "2.0 (with logging and .env)"}
    print(f"\nServer info request - {datetime.now().strftime('%H:%M:%S')}")
    return jsonify(info), 200


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("STARTING SECOND SERVER (DATA PROCESSOR)")
    print("=" * 70)
    print(f"   Address:  http://0.0.0.0:{PROCESSOR_PORT}")
    print(f"   Role:     Processing data from RabbitMQ")
    print("=" * 70)
    print("Waiting for requests from consumer...\n")
    app.run(host="0.0.0.0", port=PROCESSOR_PORT, debug=True)