from flask_cors import CORS

from flask import Flask

from config import Config

from .routes.server_bp import server_bp
from .routes.error_handlers import errors

from .database import DatabaseConnection

def init_app():
<<<<<<< HEAD
        
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app,supports_credentials=True)
=======
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

<<<<<<< HEAD
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(server_bp, url_prefix = '/servers')
    app.register_blueprint(channel_bp, url_prefix = '/channels')
    app.register_blueprint(message_bp, url_prefix = '/messages')

=======
    app.register_blueprint(server_bp, url_prefix = '/servers')
    
    app.register_blueprint(errors, url_prefix = '/errors')
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155

    return app