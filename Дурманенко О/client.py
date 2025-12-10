import requests
url = "http://127.0.0.1:5000/receive"
data = {
    "name": "Олександр",
    "surname": "Дурманенко",
    "birth_date": "2007-04-25"
}
try:
    resp = requests.post(url, json=data, timeout=5)
    print("Status:", resp.status_code)
    print("Body:", resp.json())
except requests.exceptions.RequestException as e:
    print("Error:", str(e))