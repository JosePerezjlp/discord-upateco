from flask import Blueprint

from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/register', methods=['POST'])(UserController.register)
user_bp.route('/profile', methods=['GET'])(UserController.show_profile)
user_bp.route('/logout', methods=['GET'])(UserController.logout)