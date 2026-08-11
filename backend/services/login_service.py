import jwt

from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

from repositories.user_repository import UserRepository


class LoginService:

    def __init__(self):
        self.user_repository = UserRepository()

    def login(self, email, password):

        user = self.user_repository.get_user_by_email(email)

        if not user:
            return None, "Invalid email or password"

        if not check_password_hash(
            user["password_hash"],
            password
        ):
            return None, "Invalid email or password"

        token = jwt.encode(
            {
                "user_id": user["user_id"],
                "factory_id": user["factory_id"],
                "role_id": user["role_id"],
                "exp": datetime.utcnow() + timedelta(hours=8)
            },
            "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET_KEY",
            algorithm="HS256"
        )

        return {
            "token": token,

            "user": {
                "user_id": user["user_id"],
                "full_name": user["full_name"],
                "email": user["email"],
                "factory_id": user["factory_id"],
                "role_id": user["role_id"],
                "factory_name": user["factory_name"]
            }
        }, None