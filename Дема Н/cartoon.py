class Cartoon:
    def __init__(self, name: str, year: int, genre: str):
        self.name = name
        self.year = year
        self.genre = genre
    def to_dict(self):
        return {"name": self.name, "year": self.year, "genre": self.genre}
    @staticmethod
    def input(data):
        if not isinstance(data, dict):
            return None, "input must be a dict"
        required_keys = ["name", "year", "genre"]
        for key in required_keys:
            if key not in data:
                return None, "missing required key"
        if not isinstance(data["year"], int):
            return None, "year must be a int"
        return Cartoon(data["name"], data["year"], data["genre"])