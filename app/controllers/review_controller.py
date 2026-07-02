class ReviewController:
    def __init__(self):
        self.reviews = []

    def add_review(self, user, place, rating, comment):
        self.reviews.append({
            "user": user,
            "place": place,
            "rating": rating,
            "comment": comment
        })

    def get_reviews(self, place):
        return [r for r in self.reviews if r["place"] == place]