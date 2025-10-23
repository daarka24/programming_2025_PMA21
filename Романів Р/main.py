import uuid
import json
from datetime import datetime

def read_dict(filename):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    return data

def write_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2))



def print_dict(data):
    for key, item in data.items():
        print(f"Ключ: {key}, значення:{item}")


info = json.loads(read_dict("dict.json"))
personal_id = str(uuid.uuid1())
date = str(datetime.now())

info["work_place"]["number"] = "4"
info["work_place"]["company"] = "Cool_Company"
del info["work_place"]["name"]

info["id"] = personal_id
info["update_time"] = date

some_value = info.get("1")
some_sec_value = info.get("personal_data")
print("Значення за ключем:", some_value,end="\n\n")
print("Значення за ключем:", some_sec_value,end="\n\n")
print_dict(info)

write_file("output.json", info)