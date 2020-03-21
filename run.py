# demo/__init__.py
from flask import Flask 

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return f'Hello, world from hostname: { app.config.get("HOSTNAME") }' 

    return app
