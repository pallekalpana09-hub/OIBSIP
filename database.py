import sqlite3

# Create database and table
def create_database():
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


# Save data
def save_record(name, weight, height, bmi, category):
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bmi_records(name, weight, height, bmi, category)
    VALUES (?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category))

    conn.commit()
    conn.close()


# View all records
def get_records():
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bmi_records")

    records = cursor.fetchall()

    conn.close()

    return records