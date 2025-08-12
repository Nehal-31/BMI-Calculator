
import sqlite3
from datetime import datetime

DB_NAME = "bmi_data.db"

def init_db():
    """Initialize database and create table if not exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            weight REAL,
            height REAL,
            bmi REAL,
            category TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_record(name, weight, height, bmi, category):
    """Save a BMI record to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bmi_records (name, weight, height, bmi, category, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def fetch_records():
    """Fetch all BMI records."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bmi_records ORDER BY timestamp DESC")
    records = cursor.fetchall()
    conn.close()
    return records