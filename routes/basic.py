from flask import Blueprint, request, jsonify

basic_bp = Blueprint('basic', __name__)

@basic_bp.route('/health', methods=['GET', 'POST'])
def health():
    """Health check endpoint supporting GET and POST methods."""
    return jsonify(status='OK', method=request.method)

@basic_bp.route('/course')
def course():
    """Endpoint to retrieve course info via query parameters."""
    course_name = request.args.get('course', 'Unknown')
    rating = request.args.get('rating', 'Not rated')
    return jsonify(course=course_name, rating=rating)

@basic_bp.route('/custom')
def custom_response():
    """Custom response endpoint returning JSON with status code 200."""
    return jsonify(message='Custom Response'), 200

