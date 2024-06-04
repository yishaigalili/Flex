"""
This module initializes the Flask application, configures it with environment variables,
sets up the database with SQLAlchemy, and registers blueprints for routing.
"""

import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()


def create_app():
    """
        Creates and configures an instance of the Flask application. Environment variables are used to
        set the secret key and database configuration. The SQLAlchemy database instance is initialized
        with the app, and the main blueprint for routing is registered.

        Returns:
            app: The instance of the Flask application.
        """
    app = Flask(__name__)

    app.secret_key = os.getenv('APP_SECRET_KEY')

    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_host = os.getenv('POSTGRES_HOST')
    db_port = "5432"
    db_name = os.getenv('POSTGRES_DB')
    db_uri = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)

    with app.app_context():
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
