from flask import Flask, jsonify, request
import math
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def getName():
    """
    Returns my name
    """
    nameData = {
    "name": "Pamla Chace Gore"
               }
    return jsonify(nameData)

@app.route("/hello/<name>", methods=["GET"])
def getNameMessage(name):
    """
    Returns a message
    """
    messageData = {
    "message": "Hello, there, {0}".format(name)
                  }
    return jsonify(messageData)

@app.route("/distance", methods=["POST"])
def distance():
    """
    Returns the distance between two cartesian points
    """
    r = request.get_json()
    a = r["a"]
    b = r["b"]
    s = math.hypot(a[1]-a[0],b[1]-b[0])
    data = {
        "distance": s,
        "a": a,
        "b": b
    }
    return jsonify(data)
