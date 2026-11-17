
import sqlite3
from datetime import datetime

DATABASE_NAME = "bmi_records.db"


def create_table():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bmi_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                weight REAL NOT NULL,
                height REAL NOT NULL,
                bmi REAL NOT NULL,
                category TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            )
        """)

        connection.commit()


def save_record(name, weight, height, bmi, category):
    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO bmi_records
            (name, weight, height, bmi, category, recorded_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, weight, height, bmi, category, recorded_at))

        connection.commit()


def get_user_records(name):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT weight, height, bmi, category, recorded_at
            FROM bmi_records
            WHERE name = ?
            ORDER BY recorded_at ASC
        """, (name,))

        return cursor.fetchall()
