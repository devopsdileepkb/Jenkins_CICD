from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS notes (username TEXT, note TEXT)")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    if "user" in session:
        conn = sqlite3.connect("notes.db")
        c = conn.cursor()
        c.execute("SELECT note FROM notes WHERE username=?", (session["user"],))
        notes = c.fetchall()
        conn.close()
        return render_template("dashboard.html", notes=notes)
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("notes.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
        user = c.fetchone()
        conn.close()
        if user:
            session["user"] = username
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("notes.db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?,?)", (username,password))
        conn.commit()
        conn.close()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/addnote", methods=["POST"])
def addnote():
    if "user" in session:
        note = request.form["note"]
        conn = sqlite3.connect("notes.db")
        c = conn.cursor()
        c.execute("INSERT INTO notes VALUES (?,?)", (session["user"], note))
        conn.commit()
        conn.close()
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)