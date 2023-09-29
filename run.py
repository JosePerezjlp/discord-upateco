from app import init_app
from flask_cors import CORS

if __name__ == "__main__":
    app = init_app()
    app.debug = True
    # CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500/template/login.html"}})
    app.run()