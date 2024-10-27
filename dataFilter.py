from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

import requests
import json
from urllib.parse import quote

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React app

# Initialize an empty JSON variable to hold user data
user_data = {
    "name": "aum",
    "provider": "Telus",
    "Device_Brand": "Iphone 12",
    "Device_Plan": "Leasing",
    "Gender": "Male",
    "Age": 40
}

def send_user_data(userd):
    url = 'https://new-app23-b5ff707d5b7d.herokuapp.com/get/'
    # Convert user data to JSON string
    user_data_json = json.dumps(userd)

    try:
        # Send a GET request with the user data as a parameter
        response = requests.get(url, params={'data': user_data_json})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response JSON
    except requests.exceptions.RequestException as e:
        print("Error sending user data:", e)
        return {"error": str(e)}


@app.route('/api/selected-phone', methods=['GET'])
def get_selected_phone():
    global user_data  # Declare user_data as global
    selected_phone = request.args.get('phone')
    user_data["Device_Brand"] = selected_phone

    return jsonify(user_data)  # Return the updated user data

@app.route('/api/ISP', methods=['GET'])
def get_isp():
    global user_data  # Declare user_data as global
    user_ISP = request.args.get('ISP')
    if user_ISP:
        user_data["provider"] = user_ISP  # Use user input

    return jsonify(user_data)  # Return the updated user data

@app.route('/api/option', methods=['GET'])
def get_selected_option():
    global user_data  # Declare user_data as global
    selected_option = request.args.get('selection')
    user_data["Device_Plan"] = selected_option

    return jsonify(user_data)

@app.route('/api/user_info', methods=['GET'])
def get_user_info():
    global user_data  # Declare user_data as global
    name = request.args.get('name')
    gender = request.args.get('gender')
    age = request.args.get('age')



    # Update user_data with the provided info if they exist
    if name:
        user_data["name"] = name
    if gender:
        user_data["Gender"] = gender
    if age:
        user_data["Age"] = int(age) if age.isdigit() else None

    print(send_user_data(user_data))
    return jsonify(user_data)  # Return the updated user data


app.run(debug=True, port=5000)  # Run on port 5000






