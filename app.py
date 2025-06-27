from flask import Flask
from routes import register_blueprints
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    register_blueprints(app)
    return app

# Used by 'flask run'
app = create_app()
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)     # This allows the app to be run directly with 'python app.py'