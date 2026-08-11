from database import get_db_connection


class UserRepository:

    def email_exists(self, email):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                SELECT UserID
                FROM Users
                WHERE Email = ?
                """,
                (email,)
            )

            row = cursor.fetchone()

            return row is not None

        finally:

            cursor.close()
            connection.close()


    def create_user(
        self,
        full_name,
        email,
        password_hash,
        phone
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

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

            return user_id

        finally:

            cursor.close()
            connection.close()


    def get_user_by_email(self, email):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                SELECT
                    u.UserID,
                    u.FullName,
                    u.Email,
                    u.PasswordHash,
                    u.Phone,
                    u.IsActive,
                    uf.FactoryID,
                    uf.RoleID,
                    r.RoleName,
                    f.FactoryName

                FROM Users u

                INNER JOIN UserFactory uf
                    ON u.UserID = uf.UserID

                INNER JOIN Factories f
                    ON uf.FactoryID = f.FactoryID

                INNER JOIN Roles r
                    ON uf.RoleID = r.RoleID

                WHERE u.Email = ?
                """,
                (email,)
            )

            row = cursor.fetchone()

            return row

        finally:

            cursor.close()
            connection.close()