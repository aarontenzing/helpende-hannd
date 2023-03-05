from flask import Flask, render_template, request, jsonify
import numpy as np
from queue_list import add_queue

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

user_list = []
time_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/queue",methods=["GET","POST"])
def queue():
    if request.method == "POST":
        cid = request.form["cid"]
        add_queue(cid, user_list, time_list)
        return "succes"
    else:
        return render_template('queue.html')
    
@app.route("/values")
def get_values():
    data = {"users":user_list, "time":time_list}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


