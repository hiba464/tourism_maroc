from app.models.user import User

class AuthService:
    def __init__(self):
        self.users = []

    def register(self, name, email, password):
        for u in self.users:
            if u.email == email:
                return "Email already exists ❌"

        user = User(name, email, password)
        self.users.append(user)

        return "Registered successfully ✅"

    def login(self, email, password):
        for u in self.users:
            if u.email == email and u.password == password:
                return u
        return None