from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def liveness():
    return "Server up!"


@app.route("/retrospective-provenance", methods=["POST"])
def dummy():
    return "Request received", 200
