from flask import Flask, render_template, request
import numpy as np
from queue_list import add_queue, print_queue

app = Flask(__name__)

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
        cid = request.form.get('cid')
        add_queue(cid, user_list, time_list)
        return render_template('queue.html',users=user_list,time=time_list)
    else:
        return render_template('queue.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


