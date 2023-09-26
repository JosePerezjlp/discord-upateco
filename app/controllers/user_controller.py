from ..models.auth_model import User

from flask import request, session

class UserController:

    @classmethod
    def register(cls):
       
        data = request.json
        print(f'Estoy recibiendo: {data}')        
        user = User(**data)
        
        confirm = User.confirmed_username(user)       
        if confirm != data.get('username'):
            User.create_user(user)
            return {'message': 'Cuenta creada con exito'}, 201
        else : return {'message': 'Este nombre de usuario esta en uso'}, 400
                
    
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200