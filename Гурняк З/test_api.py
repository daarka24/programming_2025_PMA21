import requests
import json
import time

SERVER1_URL = 'http://localhost:5000'

def print_response(response):
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("-" * 50)

def test_api():
    print("=" * 50)
    print("Testing REST API")
    print("=" * 50)

    print("\n1. Creating a person (blocking)...")
    response = requests.post(
        f"{SERVER1_URL}/api/persons",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "age": 30
        }
    )
    print_response(response)
    person_id = response.json().get('id')

    print("\n2. Creating a person (non-blocking)...")
    response = requests.post(
        f"{SERVER1_URL}/api/persons/async",
        json={
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "age": 25
        }
    )
    print_response(response)
    time.sleep(1)

    print("\n3. Getting all persons...")
    response = requests.get(f"{SERVER1_URL}/api/persons")
    print_response(response)

    print(f"\n4. Getting person with ID {person_id}...")
    response = requests.get(f"{SERVER1_URL}/api/persons/{person_id}")
    print_response(response)

    print(f"\n5. Updating person with ID {person_id} (blocking)...")
    response = requests.patch(
        f"{SERVER1_URL}/api/persons/{person_id}",
        json={
            "first_name": "Johnny",
            "age": 31
        }
    )
    print_response(response)

    print(f"\n6. Getting updated person with ID {person_id}...")
    response = requests.get(f"{SERVER1_URL}/api/persons/{person_id}")
    print_response(response)

    print(f"\n7. Updating person with ID {person_id} (non-blocking)...")
    response = requests.patch(
        f"{SERVER1_URL}/api/persons/{person_id}/async",
        json={
            "email": "johnny.updated@example.com"
        }
    )
    print_response(response)
    time.sleep(1)

    print(f"\n8. Deleting person with ID {person_id} (blocking)...")
    response = requests.delete(f"{SERVER1_URL}/api/persons/{person_id}")
    print_response(response)

    print(f"\n9. Trying to get deleted person with ID {person_id}...")
    response = requests.get(f"{SERVER1_URL}/api/persons/{person_id}")
    print_response(response)

    print("\n" + "=" * 50)
    print("Testing completed!")
    print("=" * 50)

if __name__ == '__main__':
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the server.")
        print("Please make sure both servers are running:")
        print("  - Server 2: python server2.py")
        print("  - Server 1: python server1.py")