class Cafe:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} - {self.location}"