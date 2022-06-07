from flask import Flask, render_template, redirect, url_for, request, session
from functions import get_add_visit_time, register
import mysql.connector
import json

app = Flask(__name__)

# Read json file for database connection credentials.
with open("credentials.json", "r") as f:
    data = json.load(f)

mydb = mysql.connector.connect(
      host="localhost",
      user=data["user"],
      password=data["password"],
      database=data["db"]
    )
    
my_cursor = mydb.cursor()

# CREATE TABLE IF NOT EXISTS.
my_cursor.execute("CREATE TABLE IF NOT EXISTS members(id INT AUTO_INCREMENT PRIMARY KEY,\
email VARCHAR(255), password VARCHAR(255), visit_time INT)")


@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if (request.method == 'POST' and request.form['submit_button']=='Login'):
        bool_val, visit_val = get_add_visit_time(request.form['username'], request.form['password'], 
                                                 data["user"], data["password"], data["db"])
        if bool_val:
            global email_val, visit_time
            email_val = request.form["username"]
            visit_time = visit_val
            return redirect(url_for('user_login_page'))
        else:
            error = "Invalid credentials. Please try again or register."
    elif (request.method == 'POST' and request.form['submit_button']=='Register'):
        if register(request.form["reg_username"], request.form["reg_password"], data["user"], data["password"], data["db"]):
            error = "User has been created."
        else:
            error = "User already exists."
    return render_template('login.html', error=error)

@app.route("/user_login_page")
def user_login_page():
    
    return f"Welcome {email_val} you visit this page {visit_time} times."


app.run(debug=True)