#!/usr/bin/env python3
"""Flask application script."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def helloworld() -> str:
    """Renders Hello world page."""
    return render_template("0-index.html", title="Welcome to Holberton")


if __name__ == "__main__":
    app.run()
