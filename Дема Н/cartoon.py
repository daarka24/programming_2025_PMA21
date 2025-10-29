def read_cartoon(filename):
    cartoon = {}
    try:
        with open("in.txt") as f:
            for line in f:
                if line.strip():
                    name, country, year = line.strip().split(", ")
                    cartoon[name] = {"Country": country, "Year": int(year)}
    except FileNotFoundError:
        print("File not found")
    return cartoon
def show_all(cartoon):
    if not cartoon:
        print("No cartoon found")
        return
    print("====All cartoons====")
    for title, info in cartoon.items():
        print(f"{title}: {info['Country']}, {info['Year']}")
def add_cartoon(cartoon):
    print("Adding cartoon")
    name = input("Enter cartoon name: ")
    if name in cartoon:
        print("Cartoon already exists")
        return
    country = input("Enter cartoon country: ")
    while True:
        year_input = input("Enter cartoon year: ")
        try:
            year = int(year_input)
            if 1900 <= year <= 2025:
                break
            else:
                print("Year must be between 1900 and 2025")
        except ValueError:
            print("Year must be between 1900 and 2025")
    cartoon[name] = {"Country": country, "Year": int(year)}
    print("Added cartoon")
def remove_cartoon(cartoon):
    print("Removing cartoon")
    name = input("Enter cartoon name: ")
    if name in cartoon:
        del cartoon[name]
        print("Removed cartoon")
    else:
        print("No cartoon found")
def edit_cartoon(cartoon):
    print("Editing cartoon")
    name = input("Enter cartoon name: ")
    if name not in cartoon:
        print("No cartoon found")
        return
    print(f"Now editing {cartoon[name]}")
    new_country = input("Enter new cartoon country: ")
    while True:
        new_year = input("Enter cartoon year: ")
        if not new_year:
            break
        try:
            year = int(new_year)
            if 1900 <= year <= 2025:
                cartoon[name]["Year"] = year
                break
            else:
                print("Year must be between 1900 and 2025")
        except ValueError:
            print("Year must be between 1900 and 2025")
    if new_country:
        cartoon[name]["Cartoon"] = new_country
    print("Cartoon edited")
def search_cartoon(cartoon):
    print("Searching cartoon")
    name = input("Enter cartoon name: ")
    if name in cartoon:
        info = cartoon[name]
        print(f"Result\n Name: {info['Country']}, {info['Year']}")
    else:
        print("No cartoon found")
def save_cartoon(cartoon):
    print("Saving cartoon")
    try:
        with open("out.txt", "w") as f:
            for name, info in cartoon.items():
                f.write(f"{name}: {info['Country']}, {info['Year']}\n")
    except FileNotFoundError:
        print("File not found")
def main():
    filename = "in.txt"
    cartoon = read_cartoon(filename)
    show_all(cartoon)
    add_cartoon(cartoon)
    remove_cartoon(cartoon)
    edit_cartoon(cartoon)
    search_cartoon(cartoon)
    show_all(cartoon)
    save_cartoon(cartoon)
if __name__ == "__main__":
    main()