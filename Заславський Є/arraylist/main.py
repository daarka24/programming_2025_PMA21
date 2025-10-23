from array_class import ArrayList


def save_to_file(my_list, filename='output.txt'):
    with open(filename, 'w') as f:
        for i in range(my_list.size):
            f.write(f"{my_list.array[i]}\t")
    print(f"Дані збережено у файл '{filename}'")


def load_from_file(my_list, filename='data.txt'):
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            numbers = content.split()
            for num in numbers:
                my_list.append(int(num))
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")


def menu_arraylist(my_list):
   while True:
        print("""\nMenu 
1. insert by index
2. pop
3. clear
4. Show ArrayList
5. append
6. save to file
0. exit
              """)
        try:
            choice = int(input("Ваш вибір: "))
        except ValueError:
            print("Введіть число!")
            continue

        if choice == 0:
            break
        elif choice == 1:
            position = int(input("Позиція: "))
            data = int(input("Дані: "))
            my_list.insert(position, data)
        elif choice == 2:
            position = int(input("Позиція: "))
            my_list.pop(position)
        elif choice == 3:
            my_list.removeAll()
            print("Список очищено")
        elif choice == 4:
            my_list.print_list()
        elif choice == 5:
            data = int(input("Дані: "))
            my_list.append(data)
        elif choice == 6:
            save_to_file(my_list)
        else:
            print("Невірний вибір!")


my_arraylist = ArrayList(8)
print ("Початкові дані:")
load_from_file(my_arraylist)
my_arraylist.print_list()
menu_arraylist(my_arraylist)

