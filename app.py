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
    #If page gets a get request, it will render the page. If no session history, creates an empty takeoff
    if request.method == "GET":
        if session.get("takeoff") is None:
            session["takeoff"] = []
            return render_template("enter_costs.html", takeoff=session["takeoff"])

    #If add line button is pressed, the values are taken from the form and added to the takeoff list
    try:
        if request.form["add_line"] == "add_line":
            item = request.form.get("item")
            size = request.form.get("size")
            unit = request.form.get("unit")
            cost = request.form.get("cost")
            note = request.form.get("note")
            line = [item, size, unit, cost, note]
            session["takeoff"].append(line)
            return render_template("enter_costs.html", takeoff=session["takeoff"])
    except: KeyError

    #If the clear table button is pressed the takeoff table is cleared and the page is reset and rendered
    try:
        if request.form["clear_table"] == "clear_table":
            session["takeoff"] = []
            return render_template("enter_costs.html", takeoff=session["takeoff"])
    except: KeyError

    #Submit the table to the database.
    try:
        if request.form["submit_to_database"] == "submit_to_database":
            #TODO
            pass
    except: KeyError

    
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