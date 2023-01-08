from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__, static_folder='./web_server/static', static_url_path='/')


@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Use this 
# flask run --host=0.0.0.0