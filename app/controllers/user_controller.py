from database.queries import add_user, get_user


class UserController:

    def register(self, name, email, password):

        return add_user(
            name,
            email,
            password
        )

    def login(self, email, password):

        user = get_user(
            email,
            password
        )

        return user