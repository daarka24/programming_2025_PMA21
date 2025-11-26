import uuid


class Person:
    def __init__(self, name, age, city, id=None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.age = age
        self.city = city

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "city": self.city
        }

    @staticmethod
    def from_dict(data):
        if "name" not in data or "age" not in data or "city" not in data:
            raise ValueError("Missing required fields")

        return Person(
            data["name"],
            data["age"],
            data["city"],
            data.get("id")
        )
