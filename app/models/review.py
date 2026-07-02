class Review:
    def __init__(self, user_name, comment, rating):
        self.user_name = user_name
        self.comment = comment
        self.rating = rating

    def __str__(self):
        return f"{self.user_name}: {self.comment} ({self.rating}/5)"