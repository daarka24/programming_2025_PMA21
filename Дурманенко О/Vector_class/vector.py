class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have same length")
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] + other.coordinates[i])
        return Vector(result)
    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have same length")
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] - other.coordinates[i])
        return Vector(result)
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Vectors must have same length")
            result = []
            for i in range(len(self.coordinates)):
                result.append(self.coordinates[i] * other.coordinates[i])
            return Vector(result)
        else:
            result = []
            for i in range(len(self.coordinates)):
                result.append(self.coordinates[i] * other)
            return Vector(result)
    def __truediv__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Vectors must have same length")
            result = []
            for i in range(len(self.coordinates)):
                if other.coordinates[i] == 0:
                    raise ValueError("Division by zero")
                result.append(self.coordinates[i] / other.coordinates[i])
            return Vector(result)
        else:
            if other == 0:
                raise ValueError("Division by zero")
            result = []
            for i in range(len(self.coordinates)):
                result.append(self.coordinates[i] / other)
            return Vector(result)
    def __str__(self):
        return "(" + ", ".join(str(x) for x in self.coordinates) + ")"
    def __len__(self):
        return len(self.coordinates)
class VectorCalculator:
    def __init__(self):
        self.first_vector = None
        self.second_vector = None
        self.multiply = None
        self.divide = None

    def read_data(self):
        try:
            with open("vectors.txt", "r") as file:
                first_line = file.readline().strip()
                second_line = file.readline().strip()
            with open("scalars.txt", "r") as file:
                multiply_line = file.readline().strip()
                divide_line = file.readline().strip()
        except:
            print("Error: Cannot read files")
            exit()
        try:
            first_vector_coords = [float(x) for x in first_line.split()]
            second_vector_coords = [float(x) for x in second_line.split()]
            self.first_vector = Vector(first_vector_coords)
            self.second_vector = Vector(second_vector_coords)
            self.multiply = float(multiply_line)
            self.divide = float(divide_line)
        except:
            print("Error: Invalid data format")
            exit()
        if len(self.first_vector) != len(self.second_vector):
            print("Error: Vectors must have same length")
            exit()
    def save_results(self, filename="result.txt"):
        try:
            with open(filename, "w") as file:
                file.write("First vector: ")
                file.write(str(self.first_vector))
                file.write("\n")
                file.write("Second vector: ")
                file.write(str(self.second_vector))
                file.write("\n")
                file.write("Sum: ")
                file.write(str(self.first_vector + self.second_vector))
                file.write("\n")
                file.write("Subtract: ")
                file.write(str(self.first_vector - self.second_vector))
                file.write("\n")
                file.write("Multiply: ")
                file.write(str(self.first_vector * self.second_vector))
                file.write("\n")
                try:
                    file.write("Divide: ")
                    file.write(str(self.first_vector / self.second_vector))
                    file.write("\n")
                except:
                    file.write("Error - division by zero\n")
                file.write(f"First vector * by ({self.multiply}): ")
                file.write(str(self.first_vector * self.multiply))
                file.write("\n")
                try:
                    file.write(f"First vector / by ({self.divide}): ")
                    file.write(str(self.first_vector / self.divide))
                    file.write("\n")
                except:
                    file.write(f"First vector / by ({self.divide}): Error - division by zero\n")
                file.write(f"Second vector * by ({self.multiply}): ")
                file.write(str(self.second_vector * self.multiply))
                file.write("\n")
                try:
                    file.write(f"Second vector / by ({self.divide}): ")
                    file.write(str(self.second_vector / self.divide))
                    file.write("\n")
                except:
                    file.write(f"Second vector / by ({self.divide}): Error - division by zero\n")
            print("Results saved")
        except:
            print("Error: Cannot write to file")
    def calculate(self):
        self.read_data()
        self.save_results()
calculator = VectorCalculator()
calculator.calculate()