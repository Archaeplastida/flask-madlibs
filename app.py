from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "wow"
debug = DebugToolbarExtension(app)

@app.route("/")
def display_homepage():
    return render_template("madlibs_input.html", words = story.prompts)

@app.route("/story")
def display_story():
    return render_template("madlibs_story.html", the_story = story.generate(request.args))