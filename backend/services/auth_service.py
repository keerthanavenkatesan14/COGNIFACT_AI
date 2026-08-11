from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

from repositories.auth_repository import AuthRepository


class AuthService:

    def __init__(self):
        self.repository = AuthRepository()
        self.secret_key = "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET_KEY"

    # ==============================
    # REGISTER
    # ==============================

    def register(self, data):

        company_name = data.get("company_name", "").strip()
        industry = data.get("industry", "").strip()
        city = data.get("city", "").strip()
        state = data.get("state", "").strip()
        full_name = data.get("full_name", "").strip()
        phone = data.get("phone", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        if not company_name:
            return False, "Company name is required"

        if not industry:
            return False, "Industry is required"

        if not city:
            return False, "City is required"

        if not state:
            return False, "State is required"

        if not full_name:
            return False, "Full name is required"

        if not email:
            return False, "Email is required"

        if not password:
            return False, "Password is required"

        if len(password) < 8:
            return False, "Password must be at least 8 characters"

        # Check email
        existing_user = self.repository.get_user_by_email(email)

        if existing_user:
            return False, "Email already registered"

        # Hash password
        password_hash = generate_password_hash(password)

        # Create factory + user
        self.repository.create_company_and_user(
            company_name=company_name,
            industry=industry,
            city=city,
            state=state,
            full_name=full_name,
            phone=phone,
            email=email,
            password_hash=password_hash
        )

        return True, "Company account created successfully"

    # ==============================
    # LOGIN
    # ==============================

    def login(self, email, password):

        email = email.strip().lower()

        user = self.repository.get_user_with_factory(email)

        if not user:
            return False, "Invalid email or password"

        if not check_password_hash(
            user["PasswordHash"],
            password
        ):
            return False, "Invalid email or password"

        token = jwt.encode(
            {
                "user_id": user["UserID"],
                "factory_id": user["FactoryID"],
                "role_id": user["RoleID"],
                "exp": datetime.utcnow() + timedelta(hours=8)
            },
            self.secret_key,
            algorithm="HS256"
        )

        # Update last login
        self.repository.update_last_login(
            user["UserID"]
        )

        response_user = {
            "user_id": user["UserID"],
            "full_name": user["FullName"],
            "email": user["Email"],
            "phone": user["Phone"],
            "factory_id": user["FactoryID"],
            "factory_name": user["FactoryName"],
            "role_id": user["RoleID"],
            "role_name": user["RoleName"]
        }

        return True, {
            "token": token,
            "user": response_user
        }