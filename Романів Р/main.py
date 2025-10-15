from functions import read_from_file

shapes = read_from_file()

with open("output_shapes.txt", "w", encoding="utf-8") as file:
    for i, el in enumerate(shapes):
        file.write(f"{i+1}. "+ str(el) + "\n")