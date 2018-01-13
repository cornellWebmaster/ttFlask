"""
Main Flask application which runs the website.
"""

from flask import Flask, render_template, request
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
app = Flask(__name__)
app_status = "block"

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
        open("data/brothers/brothers.tsv", "r") as brothers, \
        open("data/spotlight/spotlight.tsv", "r") as spotlight:
        return render_template("index.html",
                               employers=employers.readlines(),
                               schools=schools.readlines(),
                               teams=teams.readlines(),
                               eboard=eboard.readlines()[1:],
                               semester=semesterly.readlines()[1:],
                               brothers=brothers.readlines()[1:],
                               spotlights=spotlight.readlines()[1:],
                               # TODO: Switch between "block" and "none" as necessary.
                               apply_display=app_status
                               )

@app.route('/spotlight')
def spotlight_info():
    """
    Spotlight page.
    """
    id = request.args.get('id')

    with open("data/spotlight/spotlight.tsv", "r") as spotlight, \
        open("data/brothers/core.tsv", "r") as eboard:
        article = _find_article(id, spotlight.readlines())
        return render_template("spotlight.html",
                               eboard=eboard.readlines()[1:],
                               spotlight=article,
                               apply_display=app_status)

def _find_article(id, file):
    for line in file:
        line_list = line.split('\t')
        if line_list[0] == id:
            return line_list
    return [None, 
        "404 Not Found", 
        None,
        "404.jpg",
        "Sorry, this webpage could not be found."]

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
