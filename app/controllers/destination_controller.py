
class DestinationController:
    def __init__(self):
        self.destinations = ["Marrakech", "Casablanca", "Fes", "Rabat"]

    def get_all(self):
        return self.destinations

    def add(self, city):
        if city not in self.destinations:
            self.destinations.append(city)