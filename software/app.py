from flask import Flask, send_from_directory, request, jsonify
from calibration_setup import calibrate

app = Flask(__name__, static_folder='./web_server/static', static_url_path='/')


@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Create an API endpoint to talk to the frontend
@app.route("/api/start", methods=['GET'])
def api():
    # Get the data from the request
    data = request.get_json()
    # If data is not empty call calibration function
    calibrate(data) # pass in data array
    # Call calibration function
    # calibrate(data)
    # Return success
    return jsonify({'success': True})


# Use this 
# flask run --host=0.0.0.0