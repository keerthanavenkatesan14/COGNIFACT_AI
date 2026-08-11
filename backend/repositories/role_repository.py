from database import get_db_connection


class RoleRepository:

    def get_role_id(self, role_name):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                SELECT RoleID
                FROM Roles
                WHERE RoleName = ?
                """,
                (role_name,)
            )

            row = cursor.fetchone()

            if row:
                return row[0]

            return None

        finally:

            cursor.close()
            connection.close()