
import re

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

from includes import sentence_parsing_utils as utils

@app.route("/")
def home():
    return render_template("index.html", data={"response": ""})

@app.route("/noun_parse_request", methods=["POST"])
def noun_parse_request():
    if request.method == "POST":
        sentence = str(request.form["sentence"])

        if not utils.validate_sentence(sentence):
            return invalid_sentence()
        
        if not utils.sentence_has_nouns(sentence):
            return invalid_sentence()

        


def invalid_sentence():
    response = "Please provide a valid sentence with nouns."
    return render_template("index.html", data={"response": response})

