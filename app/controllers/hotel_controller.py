from controllers.reservation_controller import ReservationController

class HotelController:
    def __init__(self):
        self.hotels = []
        self.reservation_controller = ReservationController()
    def get_all(self):
        return self.hotels

    def search(self, city):
        return [h for h in self.hotels if h["city"] == city]

    def add(self, name, city, rating=0):
        self.hotels.append({
            "name": name,
            "city": city,
            "rating": rating
        })