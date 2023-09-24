from ..models.auth_model import User

from flask import request, session

class UserController:

    @classmethod
    def register(cls):
       
        data = request.json
        print(f'Estoy recibiendo: {data}')        
        user = User(**data)
        print(user)
        confirm = User.confirmed_username(user)       
        if confirm != data.get('username'):
            User.create_user(user)
            return {'message': 'Cuenta creada con exito'}, 201
        else : return {'message': 'Este nombre de usuario esta en uso'}, 400
    
    """ @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "phone_number": user.phone_number,
                "creation_date": user.creation_date,
                "last_login": user.last_login,
                "status_id": user.status_id,
                "role_id": user.role_id
            }, 200 """

    @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200