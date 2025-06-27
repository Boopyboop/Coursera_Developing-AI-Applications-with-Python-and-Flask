from flask import Blueprint, request, jsonify
import uuid

# Simulated in-memory data store (use a real DB in production)
data = []

# Create a Blueprint for person-related routes
person_bp = Blueprint('person', __name__)

@person_bp.route('/')
def index():
    """Root route for base testing."""
    return "Hello world"

@person_bp.route('/no_content')
def no_content():
    """Responds with 204 No Content status and a message."""
    return {"message": "No content found"}, 204

@person_bp.route('/exp')
def index_explicit():
    """Explicitly sets response code to 200 using a response object."""
    return {"message": "Hello World"}, 200

@person_bp.route('/data')
def get_data():
    """Check if the data list has content, returns length or error."""
    if data:
        return {"message": f"Data of length {len(data)} found"}, 200
    return {"message": "Data is empty"}, 500

@person_bp.route('/count')
def count():
    """Returns the number of items in the dataset."""
    return {"data count": len(data)}, 200

@person_bp.route('/name_search')
def name_search():
    """
    Search for a person by first name (query param: q).
    Returns 200 if found, 404 if not found, 400/422 for bad input.
    """
    query = request.args.get("q")
    if not query:
        return {"message": "Query parameter 'q' is missing"}, 400
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person.get("first_name", "").lower():
            return person, 200
    return {"message": "Person not found"}, 404

@person_bp.route("/person/<uuid:id>")
def find_by_uuid(id):
    """
    Retrieve a person by UUID.
    Args:
        id (uuid): UUID from the URL path
    Returns:
        JSON person object or 404 error
    """
    for person in data:
        if person["id"] == str(id):
            return person, 200
    return {"message": "Person not found"}, 404

@person_bp.route("/person/<uuid:id>", methods=["DELETE"])
def delete_by_uuid(id):
    """
    Delete a person by UUID.
    Returns:
        Success or 404 if not found.
    """
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message": f"Person with ID {id} deleted"}, 200
    return {"message": "Person not found"}, 404

@person_bp.route("/person", methods=["POST"])
def add_by_uuid():
    """
    Add a new person via POST JSON body.
    Expects JSON with at least an 'id' and 'first_name' field.
    """
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422

    # Validate new_person (e.g., check for required fields)
    if 'id' not in new_person or 'first_name' not in new_person:
        return {"message": "Missing required fields"}, 400

    data.append(new_person)
    return {"message": f"Person {new_person['id']} added"}, 201
