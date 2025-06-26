from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Health check endpoint supporting GET and POST
@app.route('/health', methods=['GET', 'POST'])
def health():
    return jsonify(status='OK', method=request.method)

# Endpoint to retrieve course info via query parameters
@app.route('/course')
def course():
    course_name = request.args.get('course', 'Unknown')
    rating = request.args.get('rating', 'Not rated')
    return jsonify(course=course_name, rating=rating)

# Custom response endpoint returning JSON with status code
@app.route('/custom')
def custom_response():
    return jsonify(message='Custom Response'), 200


# Main entry point to run the app
if __name__ == '__main__':
    app.run(debug=True)
