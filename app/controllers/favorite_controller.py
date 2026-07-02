from database.queries import add_favorite, get_favorites

class FavoriteController:

    def add(self, user_email, hotel_name):
        add_favorite(user_email, hotel_name)
        return "Added"

    def get(self, user_email):
        return get_favorites(user_email)