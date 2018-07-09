from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

cost_data = []

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/enter_costs", methods=["GET", "POST"])
def enter_costs():
    if request.method == "GET":
        session["takeoff"] = []
    
    if session.get("takeoff") is None:
        session["takeoff"] = []

    if request.method == "POST":
        item = request.form.get("item")
        size = request.form.get("size")
        unit = request.form.get("unit")
        cost = request.form.get("cost")
        note = request.form.get("note")
        line = [item, size, unit, cost, note]
        session["takeoff"].append(line)
    return render_template("enter_costs.html", takeoff=session["takeoff"])

@app.route("/build_project", methods=["GET"])
def build_project():
    return render_template("build_project.html")

@app.route("/view_costs", methods=["GET"])
def view_costs():
    return render_template("view_costs.html", cost_data=[])

@app.route("/extend", methods=["GET"])
def extend():
    return render_template("extend.html")

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)