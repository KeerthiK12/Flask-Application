from flask import Flask
app = Flask("Flask Application")
@app.route("/")
def home():
    return "Hello, Flask!"