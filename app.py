from flask import Flask, request, redirect, render_template
from config.db import app


# config el servidor


@app.route("/")
def index():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True)