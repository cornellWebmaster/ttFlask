from flask import Flask, render_template
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
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

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
