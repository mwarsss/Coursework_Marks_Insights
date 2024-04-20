from extensions import register_extensions
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask

# Add other extensions and their initialization code here

db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    """
    Registers all Flask extensions with the given Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    db.init_app(app)
    login_manager.init_app(app)
    app = Flask(register_extensions)

    # Add initialization for other extensions here

# Import this file in your app.py


# Example usage in app.py:
# from extensions import register_extensions
# ... app creation and configuration ...


# Register extensions with the app
register_extensions(app)
