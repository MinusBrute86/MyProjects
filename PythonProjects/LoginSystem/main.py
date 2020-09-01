from flask import Flask, render_template, redirect, url_for, session, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = "1234567890"

# Database Connection Details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'R@mpage21!'
app.config['MYSQL_DB'] = 'pythonlogin'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)


# Define routes for each HTML page
@app.route('/')
def index():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])  # POST is used to call for data from SQL and GET retrieves the data
def login():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM pythonlogin.accounts WHERE email=%s AND password=%s", (username, password))
            info = cursor.fetchone()
            if info is not None:
                if info['email'] == username and info['password'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for("profile"))
            else:
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO pythonlogin.accounts(username,password,email)VALUES(%s,%s,%s)",(username,password,email))
            mysql.connection.commit()
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route('/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template("profile.html")


@app.route('/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)