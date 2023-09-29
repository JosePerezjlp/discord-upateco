from flask import jsonify

<<<<<<< HEAD
class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code
=======
class ServerNotFound(Exception):

    def __init__(self, description = "El server solicitado no existe"):
        super().__init__()
        self.description = description
        self.status_code = 401
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
<<<<<<< HEAD
                'name': self.name,
=======
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

<<<<<<< HEAD
class ServerNotFound(CustomException):
    def __init__(self, id_server):
        description = f'El server {id_server} solicitado no existe'
        super().__init__(status_code=404, name="Server Not Found", description=description)
    
class ChannelNotFound(CustomException):

    def __init__(self, id_channel):
        description = f'El canal {id_channel} solicitado no existe'
        super().__init__(status_code=404, name="Channel Not Found", description=description)

class DatabaseError(CustomException):

    def __init__(self):
        description = "Error en la base de datos"
        super().__init__(status_code=500, name="Error en la Base de Datos", description=description)
=======
class DatabaseError(Exception):

    def __init__(self, description = "Error en la base de datos"):
        super().__init__()
        self.description = description
        self.status_code = 500

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
