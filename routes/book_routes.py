from flask import Blueprint, jsonify
import requests

# Blueprint for book-related routes
book_bp = Blueprint('book', __name__)

@book_bp.route('/book/<isbn>', methods=['GET'])
def get_book(isbn):
    """
    Retrieve book data from the Open Library API using ISBN.
    Returns:
        - 200: JSON response from Open Library
        - 404: API-specific error
        - 500: Server error or request failure
    """
    try:
        res = requests.get(
            f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json'
        )
        if res.status_code == 200:
            return jsonify(res.json()), 200
        elif res.status_code == 404:
            return {"message": "Book not found."}, 404
        else:
            return {"message": "Unexpected error from book API."}, 500
    except requests.RequestException:
        return {"message": "Failed to connect to Open Library API."}, 500

if __name__ == "__main__":
    print("book_routes.py imports and defines book_bp correctly")