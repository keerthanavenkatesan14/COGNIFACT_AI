from database import get_db_connection


class AuthRepository:

    # ==========================================
    # GET USER BY EMAIL
    # ==========================================

    def get_user_by_email(self, email):

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

            return cursor.fetchone()

        finally:

            cursor.close()
            connection.close()

    # ==========================================
    # CREATE FACTORY + USER
    # ==========================================

    def create_company_and_user(
        self,
        company_name,
        industry,
        city,
        state,
        full_name,
        phone,
        email,
        password_hash
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

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

            # ----------------------------------
            # Find ADMIN role
            # ----------------------------------

            cursor.execute(
                """
                SELECT RoleID
                FROM Roles
                WHERE RoleName = 'admin'
                """
            )

            role = cursor.fetchone()

            # If admin role doesn't exist,
            # create it.

            if not role:

                cursor.execute(
                    """
                    INSERT INTO Roles
                    (
                        RoleName,
                        Description
                    )
                    OUTPUT INSERTED.RoleID
                    VALUES
                    (
                        'admin',
                        'Factory administrator'
                    )
                    """
                )

                role_id = cursor.fetchone()[0]

            else:

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

            connection.commit()

        except Exception:

            connection.rollback()
            raise

        finally:

            cursor.close()
            connection.close()

    # ==========================================
    # GET USER + FACTORY + ROLE
    # ==========================================

    def get_user_with_factory(self, email):

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

                    f.FactoryID,
                    f.FactoryName,

                    r.RoleID,
                    r.RoleName

                FROM Users u

                INNER JOIN UserFactory uf
                    ON u.UserID = uf.UserID

                INNER JOIN Factories f
                    ON uf.FactoryID = f.FactoryID

                INNER JOIN Roles r
                    ON uf.RoleID = r.RoleID

                WHERE u.Email = ?
                  AND u.IsActive = 1
                  AND f.IsActive = 1
                """,
                (email,)
            )

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "UserID": row[0],
                "FullName": row[1],
                "Email": row[2],
                "PasswordHash": row[3],
                "Phone": row[4],
                "FactoryID": row[5],
                "FactoryName": row[6],
                "RoleID": row[7],
                "RoleName": row[8]
            }

        finally:

            cursor.close()
            connection.close()

    # ==========================================
    # UPDATE LAST LOGIN
    # ==========================================

    def update_last_login(self, user_id):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE Users
                SET LastLoginAt = GETDATE(),
                    UpdatedAt = GETDATE()
                WHERE UserID = ?
                """,
                (user_id,)
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()