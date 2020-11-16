from app import app
import json
from flask import render_template, send_from_directory

@app.route("/chart")
def chart():
    return render_template("out.html")

@app.route("/data")
def data():
    return send_from_directory("templates", "result.json")