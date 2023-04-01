from flask import Flask
from sender_app.settings import Config
from sender_app.views import socketio, blueprint

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)
    
    socketio.init_app(app)

    return app

def register_blueprints(app):
    app.register_blueprint(blueprint)
