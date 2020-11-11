from flask import Flask, request, jsonify, render_template, make_response
from qual_id.validator import Validator
from qual_id.pattern import Pattern
from qual_id.category_map import CategoryMap
from qual_id.category_map_factory import CategoryMapFactory
import random

app = Flask(__name__)


@app.route("/get/", methods=["GET"])
def get_response():
    response_obj = get_response_obj(request.args)
    response_format = request.args.get("format", "json")
    return get_response_in_format(response_obj, response_format)


@app.route("/categories/", methods=["GET"])
def categories_response():
    response = {"data": CategoryMapFactory.get("all").categories()}
    return jsonify(response)


@app.route("/badge-endpoint/", methods=["GET"])
def badge_endpoint_response():
    example = get_qual_ids("fruit-geography", "all", 1)[0]
    response_obj = {
        "schemaVersion": 1,
        "label": "Qual ID",
        "message": example,
        "color": f"hsl({random.randint(0,359)}, 100%, 50%)",
    }
    response = make_response(response_obj)
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response


def get_response_obj(args):
    pattern_string = args.get("pattern", "")
    collection_string = args.get("collection", "all")
    number = int(args.get("number", 1))

    response_obj = {}
    validator = Validator(pattern_string, collection_string)
    error = validator.error()
    if error:
        response_obj["error"] = error
    else:
        category_map = CategoryMapFactory.get(collection_string)
        pattern = Pattern(pattern_string, category_map)
        response_obj["data"] = get_qual_ids(pattern_string, collection_string, number)
    return response_obj


def get_qual_ids(pattern_string, collection_string, number):
    category_map = CategoryMapFactory.get(collection_string)
    pattern = Pattern(pattern_string, category_map)
    return [get_qual_id(pattern) for _ in range(number)]


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
