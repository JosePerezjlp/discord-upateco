from flask import Blueprint
from ..models.exceptions import ServerNotFound, DatabaseError

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(ServerNotFound)
def handle_server_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(DatabaseError)
def handle_database_error(error):
    return error.get_response(), error.status_code