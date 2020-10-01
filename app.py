from flask import Flask, request, jsonify, render_template, make_response
from qual_id.pattern import Pattern
import random

app = Flask(__name__)


@app.route('/get/', methods=['GET'])
def get_response():
  pattern = Pattern(request.args.get("pattern", ""))
  number = int(request.args.get("number", 1))

  response_obj = {}

  if not pattern.is_valid():
    response_obj["error"] = "pattern is invalid"
  else:
    response_obj["data"] = get_qual_ids(pattern, number)

  response = make_response(response_obj)
  return response


@app.route('/categories/', methods=['GET'])
def categories_response():
  response = {'data': Pattern.get_category_options()}
  return jsonify(response)


@app.route('/badge-endpoint/', methods=['GET'])
def badge_endpoint_response():
  example = get_qual_ids(Pattern('food-tool'), 1)[0]
  response_obj = {
      "schemaVersion": 1,
      "label": "Qual ID",
      "message": example,
      "color": f"hsl({random.randint(0,359)}, 100%, 50%)"
  }
  response = make_response(response_obj)
  response.headers['Cache-Control'] = 'no-cache, no-store'
  return response


def get_qual_ids(pattern, number):
  return [get_qual_id(pattern) for _ in range(number)]


def get_qual_id(pattern):
  return '-'.join([path.get_random_value() for path in pattern.get_categories()])


@app.route('/')
def index():
  return render_template('welcome.html')


if __name__ == '__main__':
  # Threaded option to enable multiple instances for multiple user access support
  app.run(threaded=True, port=5000)
