from flask import Flask
import os

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, 
                instance_relative_config=True,
                template_folder='templates')
    
    # Register blueprints
    from app import calculator
    app.register_blueprint(calculator.bp)
    
    return app