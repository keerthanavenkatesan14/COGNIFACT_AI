import pyodbc


def get_db_connection():

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=cognifact_ai;"
        "Trusted_Connection=yes;"
    )

    return pyodbc.connect(connection_string)