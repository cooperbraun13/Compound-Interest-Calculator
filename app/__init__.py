from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    
    from app import calculator
    app.register_blueprint(calculator.bp)
    
    return app