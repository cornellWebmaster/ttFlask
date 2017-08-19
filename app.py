from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open("employers.txt", "r") as employers, \
        open("schools.txt", "r") as schools, \
        open("teams.txt", "r") as teams, \
        open("core.csv", "r") as eboard, \
        open("semester.csv", "r") as semesterly, \
        open("brothers.csv", "r") as brothers:
        return render_template("index.html",
                               employers=employers.readlines(),
                               schools=schools.readlines(),
                               teams=teams.readlines(),
                               eboard=eboard.readlines()[1:],
                               semester=semesterly.readlines()[1:],
                               brothers=brothers.readlines()[1:]
                               )
