#!/usr/bin/env python3
"""Flask application script."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
from typing import Union, Dict
import pytz
from datetime import datetime

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


@babel.localeselector
def get_locale() -> str:
    """Select a language translation."""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config["LANGUAGES"]:
            return locale

    locale = request.headers.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """Select a timezone translation."""
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            if timezone:
                return pytz.timezone(timezone)
        elif g.user:
            timezone = g.user.get("timezone")
            if timezone:
                return pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            return pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = app.config["BABEL_DEFAULT_TIMEZONE"]

    return timezone


@app.route("/", strict_slashes=False)
def helloworld() -> str:
    """Renders Hello world page."""
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    current_time = format_datetime(datetime=current_time)
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run()
