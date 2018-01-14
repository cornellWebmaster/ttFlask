"""
Main Flask application which runs the website.
"""

from flask import Flask, render_template, request
import os
import sys

reload(sys)
sys.setdefaultencoding("utf8")
app = Flask(__name__)

# TODO: Switch between "block" and "none" as necessary.
app_status = "block" # Enables/disables rush applications.
                     # Toggle between "block" and "none"

@app.route('/')
def main_page(): 
    """
    Main page of website.
    """
    with open("data/portfolio/employers.txt", "r") as employers, \
        open("data/portfolio/schools.txt", "r") as schools, \
        open("data/portfolio/teams.txt", "r") as teams, \
        open("data/brothers/core.tsv", "r") as eboard, \
        open("data/brothers/semester.tsv", "r") as semesterly, \
        open("data/brothers/brothers.tsv", "r") as brothers, \
        open("data/spotlight/carousel.tsv", "r") as carousel:
        return render_template("index.html",
                               employers=employers.readlines(),
                               schools=schools.readlines(),
                               teams=teams.readlines(),
                               eboard=eboard.readlines()[1:],
                               semester=semesterly.readlines()[1:],
                               brothers=brothers.readlines()[1:],
                               carousel=carousel.readlines()[1:],
                               apply_display=app_status
                               )

@app.route('/spotlight')
def spotlight_page():
    """
    Spotlight page. Takes in a unique 8-char ID and maps it to
    the corresponding spotlight article if it exists.

    If the ID is not found, then redirects to 404 page.
    """
    id = request.args.get('id')

    with open("data/spotlight/spotlight.tsv", "r") as spotlight, \
        open("data/brothers/core.tsv", "r") as eboard:
        article = _find_article(id, spotlight.readlines())
        if article == None:
            return render_template("404.html",
                                   eboard=eboard.readlines()[1:],
                                   path="this",
                                   apply_display=app_status)
        else:
            return render_template("spotlight.html",
                                   eboard=eboard.readlines()[1:],
                                   spotlight=article,
                                   apply_display=app_status)

@app.route('/<path:path>')
def page_not_found(path):
    """
    Page for nonexistent pages on website.
    """
    with open("data/brothers/core.tsv", "r") as eboard:
        return render_template("404.html",
                               eboard=eboard.readlines()[1:],
                               path=path,
                               apply_display=app_status)

def _find_article(id, file):
    """
    Given contents of spotlight.tsv file, will find the row
    which corresponds to the given ID.
    """
    for line in file:
        line_list = line.split('\t')
        if line_list[0] == id:
            return line_list
    return None

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
