class Favorite:
    def __init__(self, user_email, item_name):
        self.user_email = user_email
        self.item_name = item_name

    def __str__(self):
        return f"{self.item_name} "