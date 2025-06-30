# routes/mathematics.py

from flask import Blueprint, jsonify, request

math_bp = Blueprint('math', __name__)

@math_bp.route('/math/sum', methods=['GET'])
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': summation(a, b)})

@math_bp.route('/math/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': subtraction(a, b)})

@math_bp.route('/math/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': multiplication(a, b)})

# Core logic
def summation(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
