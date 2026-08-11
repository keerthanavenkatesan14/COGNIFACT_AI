from database import get_db_connection


class FactoryRepository:

    def create_factory(
        self,
        factory_name,
        industry,
        city,
        state
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

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
                    factory_name,
                    industry,
                    city,
                    state
                )
            )

            factory_id = cursor.fetchone()[0]

            return factory_id

        finally:

            cursor.close()
            connection.close()