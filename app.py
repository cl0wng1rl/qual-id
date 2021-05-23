from flask import Flask, request, jsonify, render_template, make_response
from qual_id.groups import GroupFactory
from qual_id.api import API
import random

app = Flask(__name__)


@app.route("/get/", methods=["GET"])
def get_response():
    return make_response(API.run(request.args))


@app.route("/categories/", methods=["GET"])
def categories_response():
    group_string = request.args.get("group", "all")
    if not GroupFactory.has(group_string):
        return jsonify({"error": "invalid group: %s" % (group_string)})
    return jsonify({"data": GroupFactory.get(group_string).info()})


@app.route("/badge-endpoint/", methods=["GET"])
def badge_endpoint_response():
    badge_args = {"categories": "fruit-geography", "format": "csv", "number": "1"}
    response = make_response(get_badge_response_object(API.run(badge_args)))
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response


def get_badge_response_object(message):
    return {
        "schemaVersion": 1,
        "label": "Qual ID",
        "message": message,
        "color": f"hsl({random.randint(0,359)}, 100%, 50%)",
    }


@app.route("/")
def index():
    return render_template("welcome.html")


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
