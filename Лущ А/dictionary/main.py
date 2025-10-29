from cars import *

INPUT_FILE = "cars_input.txt"
OUTPUT_FILE = "cars_output.txt"

def main_menu():
    cars_database = load_from_file(INPUT_FILE)

    while True:
        print("\n=== Cars Database Menu ===")
        print("1. Display all cars")
        print("2. Display single car")
        print("3. Add new car")
        print("4. Delete car")
        print("5. Update car information")
        print("6. Save to file")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_cars(cars_database)
        elif choice == "2":
            reg_number = input("Enter registration number: ")
            display_single_car(cars_database, reg_number)
        elif choice == "3":
            reg_number = input("Enter registration number: ")
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            owner = input("Enter owner: ")
            probig = input("Enter probig: ")
            add_new_car(cars_database, reg_number, brand, model, year, owner, probig)
        elif choice == "4":
            reg_number = input("Enter registration number to delete: ")
            delete_car(cars_database, reg_number)
        elif choice == "5":
            reg_number = input("Enter registration number: ")
            field_name = input("Enter field to update (brand, model, year, owner, probig): ")
            new_value = input("Enter new value: ")
            update_car_information(cars_database, reg_number, field_name, new_value)
        elif choice == "6":
            save_to_file(cars_database, OUTPUT_FILE)
        elif choice == "7":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()
