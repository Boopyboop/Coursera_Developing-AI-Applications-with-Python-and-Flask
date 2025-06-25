from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<b>My first Flask application in action!</b>"

@app.route("/json")
def return_json():
    return jsonify({"message": "Hello, JSON!"})
