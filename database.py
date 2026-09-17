import sqlite3

def create_database():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            body TEXT,
            category TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_email(sender, subject, body, category):
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emails (sender, subject, body, category)
        VALUES (?, ?, ?, ?)
    """, (sender, subject, body, category))

    conn.commit()
    conn.close()
