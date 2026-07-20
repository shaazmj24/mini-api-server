import sqlite3

DATABASE_PATH = "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    # Lets us access columns by name: row["title"]. without it, it returns tuple . want dictionary cuz easier that way 
    connection.row_factory = sqlite3.Row          

    return connection


def initialize_database() -> None:
    connection = get_connection()
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
            """
        )

        result = connection.execute(
            "SELECT COUNT(*) AS task_count FROM tasks"
        )
        row = result.fetchone()

        if row["task_count"] == 0:
            connection.executemany(
                """
                INSERT INTO tasks (title, done)
                VALUES (?, ?)
                """,
                [
                    ("Grocery", 0),
                    ("one leetcode", 0),
                    ("complete application", 1),
                ],
            )

        connection.commit()

    finally:
        connection.close()
        
        
        
        

