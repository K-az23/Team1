# Pure DB connection test, does not need flask to start.


from db.connection import get_connection


def test_database_connection():
    connection = None

    try:
        connection = get_connection()

        if connection.is_connected():
            print("Connected to Executive Parlor database successfully.")

            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")

            database_name = cursor.fetchone()[0]

            print(f"Connected schema: {database_name}")

            cursor.close()

    except Exception as error:
        print(f"Database connection failed: {error}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("Database connection returned to pool.")


if __name__ == "__main__":
    test_database_connection()