#!/usr/bin/env python3
"""Flask application script."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext

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


@app.before_request
def get_user(login_as):
    """Get user from request."""
    if login_as and int(login_as) in users:
        return users[int(login_as)]
    return None


@app.before_request
def before_request():
    """Get user from request."""
    login_as = request.args.get("login_as")
    g.user = get_user(login_as)


@app.route("/")
def helloworld():
    """Renders Hello world page."""
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """Select a language translation."""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5500)
