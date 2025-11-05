import json

def display_all_foods(foods_dict):
    print("\n=== All Foods ===")
    for item_id, food in foods_dict.items():
        print(f"ID: {item_id}")
        for key, value in food.items():
            print(f"  {key}: {value}")
        print()

def display_single_food(foods_dict, item_id):
    try:
        print(f"\n=== Food {item_id} ===")
        for key, value in foods_dict[item_id].items():
            print(f"{key}: {value}")
    except:
        print(f"Food {item_id} not found")

def add_new_food(foods_dict, item_id, name, category, calories, price, is_vegetarian):
    foods_dict[item_id] = {
        "name": name,
        "category": category,
        "calories": calories,
        "price": price,
        "is_vegetarian": is_vegetarian
    }
    print(f"Food {item_id} added successfully")

def delete_food(foods_dict, item_id):
    try:
        del foods_dict[item_id]
        print(f"Food {item_id} deleted successfully")
    except:
        print(f"Food {item_id} not found")

def update_food_information(foods_dict, item_id, field_name, new_value):
    try:
        foods_dict[item_id][field_name] = new_value
        print(f"Food {item_id} updated successfully")
    except:
        print("Update failed")

def save_to_file(foods_dict, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(foods_dict, f, indent=4)
        print(f"Data saved to {file_path}")
    except:
        print("Save failed")

def load_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except:
        print("Load failed")
        return {}

def main_menu():
    foods_dict = {}
    data_file = input("Enter database filename to load: ")
    foods_dict = load_from_file(data_file)

    while True:
        print("\n=== Food Database Menu ===")
        print("1. Display all foods")
        print("2. Display single food")
        print("3. Add new food")
        print("4. Delete food")
        print("5. Update food information")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_foods(foods_dict)

        elif choice == "2":
            fid = input("Enter food ID: ")
            display_single_food(foods_dict, fid)

        elif choice == "3":
            fid = input("Enter food ID: ")
            name = input("Enter name: ")
            category = input("Enter category (e.g., fruit, drink, main, dessert): ")
            calories = int(input("Enter calories (kcal): "))
            price = float(input("Enter price: "))
            veg_input = input("Is vegetarian? (y/n): ").strip().lower()
            is_vegetarian = veg_input in ("y", "yes", "1", "true", "t")
            add_new_food(foods_dict, fid, name, category, calories, price, is_vegetarian)

        elif choice == "4":
            fid = input("Enter food ID to delete: ")
            delete_food(foods_dict, fid)

        elif choice == "5":
            fid = input("Enter food ID: ")
            field_name = input("Enter field name to update (name/category/calories/price/is_vegetarian): ")
            new_value = input("Enter new value: ")
            update_food_information(foods_dict, fid, field_name, new_value)

        elif choice == "6":
            data_file = input("Enter filename: ")
            save_to_file(foods_dict, data_file)

        elif choice == "7":
            data_file = input("Enter filename: ")
            foods_dict = load_from_file(data_file)

        elif choice == "8":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

main_menu()
