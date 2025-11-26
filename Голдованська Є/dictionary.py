import json
def read_json(filename):
    with open(filename, encoding="UTF-8") as file:
        return json.load(file)

def write_json(filename, data):
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(data,file,indent=2)

dic = read_json("in.json")

for key,item in dic.items():
    print(f"key: {key}, item: {item}")

del dic["aeropress"]
del dic["black_orange"]["method"]

dic["cold_brew"]={"price":120, "bean":"Colombia", "method":"cold_brew"}

dic["latte_caramel"]["price"] = 150

write_json("out.json", dic)