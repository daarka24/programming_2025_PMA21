library= {}

try:
    with open('starters.txt', 'r') as file:
        for line in file:
          try:
            title, author, year= line.strip().split(';')
            library[title]={"author": author, "year": year }
          except ValueError:
              print(f"Wrong line, skipping...: {line.strip()}")

except FileNotFoundError:
    print("No starters.txt file")
except Exception as error:
    print("Something went wrong", error)


try:
    library["Happy Place"] = {"author": "Emily Henry", "year": 2023}
    library["Things We Never Got Over"] = {"author": "Lucy Score", "year": 2022}
    library["Red, White & Royal Blue"] = {"author": "Casey McQuiston", "year": 2019}


    if "Love and Other Words" in library:
        library["Love and Other Words"]["author"] = "C. Lauren"


    if "Me Before You" in library:
        library["Me Before You"]["year"] = 2013


    library.pop("The Spanish Love Deception", None)
except Exception as error:
    print("error while working with dictionary", error)


try:

    with open('result.txt', 'w') as file:
        file.write("Current library: \n")
        for title, info in library.items():
            file.write(f'{title} - author:{info["author"]}, year: {info["year"]}\n')
except FileNotFoundError:
    print("No result.txt file")
except Exception as error:
    print("Something went wrong with result file", error)