#!/usr/bin/env python3
"""Flask application script."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union, Dict

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get user from request."""
    login_as = request.args.get("login_as")
    if login_as and int(login_as) in users:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request() -> None:
    """Get user from request."""
    user = get_user()
    g.user = user


@app.route("/", strict_slashes=False)
def helloworld() -> str:
    """Renders Hello world page."""
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """Select a language translation."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run()
