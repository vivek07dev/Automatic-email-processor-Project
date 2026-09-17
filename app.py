from flask import Flask, render_template
from database import create_database, add_email
from email_processor import process_email
import sqlite3

app = Flask(__name__)
create_database()


@app.route("/")
def home():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT*FROM email ORDER BY idDESC")
    email = cursor.fetchall()
    conn.close()

    return render_template("index.html",emails=email)


@app.route("/test-email")
def test_email():

    sender = "test@example.com"
    subject = "Important meeting"
    body = "This is an important email."


    category = process_email(sender, subject, body)

    add_email(sender, subject, body, category)

    return "Email processed successfully!"


if __name__ == "_main_":
    app.run(debug=True)
