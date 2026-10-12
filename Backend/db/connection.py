# db/connection.py

import os
from pathlib import Path

from dotenv import load_dotenv
from mysql.connector import pooling, Error



# Load environment variables
# ----------------------

# Points to Backend/.env regardless of where Python is run from
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=ENV_PATH)



# Database connection pool
# This is to help overhead resources with the DB, by restricting about of new connections established.
# -----------------------------------

try:
    db_pool = pooling.MySQLConnectionPool(
        pool_name="executive_parlor_pool",
        pool_size=5,
        pool_reset_session=True,

        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

except Error as error:
    print(f"Database connection pool failed: {error}")
    db_pool = None



# Get database connection
# -----------------------

def get_connection():
    if db_pool is None:
        raise RuntimeError(
            "Database connection pool is not available."
        )

    try:
        return db_pool.get_connection()

    except Error as error:
        raise RuntimeError(
            f"Unable to get database connection: {error}"
        ) from error