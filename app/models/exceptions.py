from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

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