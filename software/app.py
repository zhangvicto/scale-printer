from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__)
static_path = './web_server/static'

@app.route("/")
def index():
    return send_from_directory('index.html', static_path)

# Use this 
# flask run --host=0.0.0.0