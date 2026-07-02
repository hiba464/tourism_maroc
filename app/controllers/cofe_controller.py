class CafeController:
    def __init__(self):
        self.cafes = ["Cafe Central", "Cafe Relax"]

    def get_all(self):
        return self.cafes

    def add(self, name):
        self.cafes.append(name)