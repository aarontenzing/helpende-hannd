from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

users = []
users.append(["10","time:17:02"])
users.append(["11","time:17:04"])



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/queue",methods=["GET","POST"])
def get_queue():
    if request.method == "POST":
        cid = request.form.get('cid')
        print(cid)
        users.append(cid)
        return render_template('queue.html',cid=cid)
    else:
        return render_template('queue.html')

def post_queue():
    data = request.form['data']
    return render_template('queue.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


