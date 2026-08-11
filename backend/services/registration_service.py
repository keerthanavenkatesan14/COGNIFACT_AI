from database import get_db_connection

from werkzeug.security import generate_password_hash


class RegistrationService:

    def register_company(
        self,
        company_name,
        industry,
        city,
        state,
        full_name,
        phone,
        email,
        password
    ):

        connection = None
        cursor = None

        try:

            connection = get_db_connection()
            cursor = connection.cursor()

            # ----------------------------------
            # Check existing email
            # ----------------------------------

            cursor.execute(
                """
                SELECT UserID
                FROM Users
                WHERE Email = ?
                """,
                (email,)
            )

            if cursor.fetchone():

                raise ValueError(
                    "Email already registered"
                )


            # ----------------------------------
            # Create factory
            # ----------------------------------

            cursor.execute(
                """
                INSERT INTO Factories
                (
                    FactoryName,
                    Industry,
                    City,
                    State
                )

                OUTPUT INSERTED.FactoryID

                VALUES (?, ?, ?, ?)
                """,
                (
                    company_name,
                    industry,
                    city,
                    state
                )
            )

            factory_id = cursor.fetchone()[0]


            # ----------------------------------
            # Create user
            # ----------------------------------

            password_hash = generate_password_hash(
                password
            )

            cursor.execute(
                """
                INSERT INTO Users
                (
                    FullName,
                    Email,
                    PasswordHash,
                    Phone
                )

                OUTPUT INSERTED.UserID

                VALUES (?, ?, ?, ?)
                """,
                (
                    full_name,
                    email,
                    password_hash,
                    phone
                )
            )

            user_id = cursor.fetchone()[0]


            cursor.execute(
                """
                SELECT RoleID
                FROM Roles
                WHERE RoleName = ?
                """,
                ("ADMIN",)
            )

            role = cursor.fetchone()

            if not role:

                raise ValueError(
                    "ADMIN role does not exist. "
                    "Please insert roles into the Roles table."
                )

            role_id = role[0]


            # ----------------------------------
            # Connect user to factory
            # ----------------------------------

            cursor.execute(
                """
                INSERT INTO UserFactory
                (
                    UserID,
                    FactoryID,
                    RoleID,
                    IsPrimary
                )

                VALUES (?, ?, ?, 1)
                """,
                (
                    user_id,
                    factory_id,
                    role_id
                )
            )


            # ----------------------------------
            # Commit everything
            # ----------------------------------

            connection.commit()


            return {
                "user_id": user_id,
                "factory_id": factory_id,
                "message":
                    "Company account created successfully"
            }


        except Exception:

            if connection:
                connection.rollback()

            raise


        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()