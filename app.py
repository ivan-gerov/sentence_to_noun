from includes.sentence_parsing_utils import SentenceParser, InvalidSentenceError

import sys

from flask import Flask, render_template, request, Blueprint


route_blueprint = Blueprint("route_blueprint", __name__)


@route_blueprint.route("/")
def home():
    return render_template("index.html", data={"response": ""})


@route_blueprint.route("/parse_sentence", methods=["POST"])
def parse_sentence_request():
    if request.method == "POST":
        sentence_string = str(request.form["sentence"])

        try:
            sentence_parser = SentenceParser(sentence_string)
            print(sentence_parser.sentence_string, file=sys.stderr)
            nouns = ", ".join(sentence_parser.get_nouns())
            print(nouns, file=sys.stderr)
        except InvalidSentenceError:
            return invalid_sentence(sentence_string)

        if not nouns:
            return invalid_sentence(sentence_string)

        response = [
            f"Your sentence - <strong>{sentence_parser.sentence_string}</strong>",
            "<br>contains the following nouns:",
            f"<br><br><strong>[{nouns}]</strong>",
        ]

        return render_template("index.html", data={"response": "".join(response)})


def invalid_sentence(sentence_string):
    """
    Response to be sent to the client in case the sentence they've provided
    is not valid (doesn't contain any alphabetical chars) or if the sentence
    doesn't have any nouns.
    """
    response = [
        "Please provide a valid sentence with nouns.",
        f"<br>You have provided --> <strong>{sentence_string}</strong>",
    ]
    return render_template("index.html", data={"response": "".join(response)})


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    app.register_blueprint(route_blueprint)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
