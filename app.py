"""
Main Flask application which runs the website.
"""

from flask import Flask, render_template
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
app = Flask(__name__)

@app.route('/')
def hello_world(): 
    """
    Main function.

    NOTE: To enable rush applications, let apply_display="block".
    To disable, let apply_display="none".
    """
    with open("data/places/employers.txt", "r") as employers, \
        open("data/places/schools.txt", "r") as schools, \
        open("data/places/teams.txt", "r") as teams, \
        open("data/brothers/core.tsv", "r") as eboard, \
        open("data/brothers/semester.tsv", "r") as semesterly, \
        open("data/brothers/brothers.tsv", "r") as brothers:
        return render_template("index.html",
                               employers=employers.readlines(),
                               schools=schools.readlines(),
                               teams=teams.readlines(),
                               eboard=eboard.readlines()[1:],
                               semester=semesterly.readlines()[1:],
                               brothers=brothers.readlines()[1:],
                               # TODO: Switch between "block" and "none" as necessary.
                               apply_display="block"
                               )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
