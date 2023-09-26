from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.auth_pb import auth_bp
from .routes.user_bp import user_bp
from .database import DatabaseConnection

def init_app():
        
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app,supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(auth_bp, url_prefix='/auth')

    app.register_blueprint(user_bp, url_prefix='/app')

    return app