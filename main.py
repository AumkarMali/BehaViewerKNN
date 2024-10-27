# app.py
import os
from flask import Flask, request, jsonify
from predictorClass import gradientBoostingClassifier  # Import functions from main.py
import json

app = Flask(__name__)


# Endpoint for predictions
@app.route('/get/', methods=['GET'])
def respond():
    user_input_text = request.args.get("data", None)
    if user_input_text:
        try:
            # Decode the JSON string from the request
            new_user_data = json.loads(user_input_text)  # Parse the incoming JSON string

            # Call the classifier with the JSON string representation
            predicted_class, predicted_provider = gradientBoostingClassifier(json.dumps(new_user_data))

            response = {
                "predicted_class": predicted_class,
                "predicted_provider": predicted_provider
            }
            print(response)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON data"}
    else:
        response = {"error": "No data provided"}

    return jsonify(response)


# Default index endpoint
@app.route('/')
def index():
    return "Welcome to the ---BACKEND---"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's PORT or default to 5000
    app.run(host='0.0.0.0', port=port, threaded=True)  # Bind to host 0.0.0.0 for external access
