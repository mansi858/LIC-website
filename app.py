from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():

    data = request.get_json()

    conn = sqlite3.connect("insurance.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS inquiries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        email TEXT,
        message TEXT
    )
    """)

    cur.execute("""
    INSERT INTO inquiries(name, mobile, email, message)
    VALUES (?, ?, ?, ?)
    """, (
        data["name"],
        data["mobile"],
        data["email"],
        data["message"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Inquiry Submitted Successfully"})

if __name__ == "__main__":
    app.run(debug=True)

    

    