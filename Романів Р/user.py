import uuid

class User:
    def __init__(self, name, age, city, id=None, job=None):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        self.id = id or str(uuid.uuid1())

    def to_dict(self):
        return {"name": self.name, "age": self.age, "city": self.city, "id": self.id, "job": self.job}

    @staticmethod
    def from_dict(data):
        id = data.get("id", None)
        job = data.get("job", None)
        return User(data["name"], data["age"], data["city"], id, job)