from flask import Flask, render_template


app = Flask(__name__)

@app.route("/") #Decorator -  root url of the website
def home_page():
    return render_template('home.html')

@app.route("/about/<username>")
def about(username):
    return f"<h1> About Page of {username} </h1>"
