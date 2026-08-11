class UserModel:

    def __init__(
        self,
        user_id=None,
        full_name=None,
        email=None,
        password_hash=None,
        phone=None,
        email_verified=False,
        is_active=True,
        last_login_at=None,
        created_at=None,
        updated_at=None
    ):

        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash
        self.phone = phone
        self.email_verified = email_verified
        self.is_active = is_active
        self.last_login_at = last_login_at
        self.created_at = created_at
        self.updated_at = updated_at