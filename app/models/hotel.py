class Hotel:
    def __init__(self, name, city, price):
        self.name = name
        self.city = city
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.city} - {self.price} MAD"