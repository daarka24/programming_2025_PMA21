def display_all_cars(database):
    print("\n=== All Cars ===")
    for reg_number, car_info in database.items():
        print(f"Registration: {reg_number}")
        for key, value in car_info.items():
            print(f"  {key}: {value}")
        print()

def display_single_car(database, reg_number):
    if reg_number in database:
        print(f"\n=== Car {reg_number} ===")
        for key, value in database[reg_number].items():
            print(f"{key}: {value}")
    else:
        print(f"Car {reg_number} not found")

def add_new_car(database, reg_number, brand, model, year, owner, probig):
    database[reg_number] = {
        "brand": brand,
        "model": model,
        "year": year,
        "owner": owner,
        "probig": probig
    }
    print(f"Car {reg_number} added successfully")

def delete_car(database, reg_number):
    if reg_number in database:
        del database[reg_number]
        print(f"Car {reg_number} deleted successfully")
    else:
        print(f"Car {reg_number} not found")

def update_car_information(database, reg_number, field_name, new_value):
    if reg_number in database and field_name in database[reg_number]:
        database[reg_number][field_name] = new_value
        print(f"Car {reg_number} updated successfully")
    else:
        print("Update failed")

def save_to_file(database, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for reg_number, info in database.items():
                line = f"{reg_number},{info['brand']},{info['model']},{info['year']},{info['owner']},{info['probig']}\n"
                f.write(line)
        print(f"Data saved to {filename}")
    except:
        print("Save failed")

def load_from_file(filename):
    database = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    reg_number = parts[0]
                    database[reg_number] = {
                        "brand": parts[1],
                        "model": parts[2],
                        "year": parts[3],
                        "owner": parts[4],
                        "probig": parts[5]
                    }
        print(f"Data loaded from {filename}")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty database.")
    return database
