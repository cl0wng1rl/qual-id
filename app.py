from flask import Flask, request, jsonify, render_template, make_response
from qual_id.pattern import Pattern
from qual_id.category_map import CategoryMap
from qual_id.category_map_factory import CategoryMapFactory
import random

app = Flask(__name__)


@app.route("/get/", methods=["GET"])
def get_response():
    return get_response_with_category_map(CategoryMapFactory.all())


@app.route("/categories/", methods=["GET"])
def categories_response():
    response = {"data": CategoryMap.all()}
    return jsonify(response)


@app.route("/badge-endpoint/", methods=["GET"])
def badge_endpoint_response():
    example = get_qual_ids(Pattern("fruit-geography"), 1)[0]
    response_obj = {
        "schemaVersion": 1,
        "label": "Qual ID",
        "message": example,
        "color": f"hsl({random.randint(0,359)}, 100%, 50%)",
    }
    response = make_response(response_obj)
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response


def get_response_with_category_map(category_map):
    pattern_string = request.args.get("pattern", "")
    pattern = Pattern(pattern_string, category_map)
    number = int(request.args.get("number", 1))

    response_obj = get_qual_ids(pattern, number)

    response_format = request.args.get("format", "json")
    return get_response_in_format(response_obj, response_format)


def get_qual_ids(pattern, number):
    response_obj = {}
    error = pattern.error()
    if error:
        response_obj["error"] = error
    else:
        response_obj["data"] = [get_qual_id(pattern) for _ in range(number)]
    return response_obj


def get_qual_id(pattern):
    return "-".join([category.random() for category in pattern.get_categories()])


def get_response_in_format(response_obj, response_format):
    if response_format == "csv":
        return make_response(",".join(response_obj["data"]) or response_obj["error"])
    return make_response(response_obj)


@app.route("/")
def index():
    return render_template("welcome.html")


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
