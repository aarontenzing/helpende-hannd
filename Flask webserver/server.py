from flask import Flask, render_template, request, jsonify
import numpy as np
from queue_list import add_queue
from write_json import write

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

user_list = []
time_list = []

class_list = []
member_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/queue",methods=["GET","POST"])
def queue():
    if request.method == "POST":
        cid = request.form["cid"]
        tmp = add_queue(cid, user_list, time_list)
        return "succes"
    else:
        return render_template('queue.html')
    
@app.route("/values")
def get_values():
    data = {"users":user_list, "time":time_list}
    return jsonify(data)

@app.route("/class", methods=["POST","GET"])
def create_class():
    if request.method == "POST":  

        return jsonify()
    else:
        return render_template("class_form.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


