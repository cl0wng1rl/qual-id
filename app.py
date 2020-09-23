# app.py
from flask import Flask, request, jsonify, render_template
from src.Pattern import Pattern
import random

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def respond():
    pattern = Pattern(request.args.get("pattern", ""))
    number = int(request.args.get("number", 1))

    response = {}

    if not pattern.is_valid():
        response["error"] = "pattern is invalid"
    else:
        response["data"] = get_qual_ids(pattern, number)
    return jsonify(response)

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