from flask import Blueprint

from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

<<<<<<< HEAD
server_bp.route('/data', methods=['GET'])(ServerController.get_all)
server_bp.route('/get/<int:id_server>', methods=['GET'])(ServerController.get)
server_bp.route('/create', methods=['POST'])(ServerController.create)
=======
server_bp.route('/', methods=['GET'])(ServerController.get_all)
server_bp.route('/<int:id_server>', methods=['GET'])(ServerController.get)
server_bp.route('/', methods=['POST'])(ServerController.create)
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
server_bp.route('/<int:id_server>', methods=['PUT'])(ServerController.update)
server_bp.route('/<int:id_server>', methods=['DELETE'])(ServerController.delete)