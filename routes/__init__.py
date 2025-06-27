from .basic import basic_bp
from .book_routes import book_bp
from .person_routes import person_bp

def register_blueprints(app):
    app.register_blueprint(basic_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(person_bp)
