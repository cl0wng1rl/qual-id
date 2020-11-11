from flask import Flask, request, jsonify, render_template, make_response
from qual_id.response import Response
from qual_id.category_map_factory import CategoryMapFactory
import random

app = Flask(__name__)


@app.route("/get/", methods=["GET"])
def get_response():
    return make_response(Response(request.args).get_response_obj())


@app.route("/categories/", methods=["GET"])
def categories_response():
    collection_string = request.args.get("collection", "all")
    if not CategoryMapFactory.has(collection_string):
        return jsonify({"error": "invalid collection: %s" % (collection_string)})
    return jsonify({"data": CategoryMapFactory.get(collection_string).categories()})


@app.route("/badge-endpoint/", methods=["GET"])
def badge_endpoint_response():
    qual_id = Response({"pattern": "fruit-geography"}).get_qual_ids()[0]
    response = make_response(get_badge_response_object(qual_id))
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
