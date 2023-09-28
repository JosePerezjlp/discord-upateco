from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.auth_pb import auth_bp
from .routes.server_bp import server_bp
from .routes.channel_bp  import channel_bp
from .routes.message_bp import message_bp

from .database import DatabaseConnection

def init_app():
        
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app,supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(server_bp, url_prefix = '/servers')
    app.register_blueprint(channel_bp, url_prefix = '/channels')
    app.register_blueprint(message_bp, url_prefix = '/messages')


    return app