#!/usr/bin/env python3
"""Flask application script."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def helloworld():
    """Renders Hello world page."""
    return render_template("3-index.html", title="Welcome to Holberton")


@babel.localeselector
def get_locale():
    """Select a language translation."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5500)
