# app.py
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def respond():
    pattern = request.args.get("pattern", None)
    print(f"pattern={pattern}")
    response = {}

    if not pattern:
        response["error"] = "no pattern found"
    elif str(pattern).isdigit(): # placeholder for incorrect pattern format
        response["error"] = "name can't be numeric."
    else:
        response["data"] = get_qual_id(pattern)
    return jsonify(response)

def get_qual_id(pattern):
  return get_qual_id_for(pattern.split('-'))

def get_qual_id_for(categories):
  return '-'.join([get_name(category) for category in categories])
    

def get_name(category):
  data_file = open(f"data/{category}.txt", "r")
  data_list = data_file.read().split("\n")
  return random.choice(data_list)

def get_qual_ids():
  return f"{get_name('food')}-{get_name('animal')}"

@app.route('/')
def index():
    return render_template('welcome.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)