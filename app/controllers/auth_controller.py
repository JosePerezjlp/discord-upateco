from ..models.auth_model import User

from flask import request, session

class AuthController:

    @classmethod
    def login(cls):
        data = request.json
        print(data)
        user = User(**data)        
        exist = User.is_registered(user)   
        resultado_string = str(exist[0])   
        if exist is not None:
          
            session['username'] = data.get('username')
            data_user = {"id":resultado_string,"username":data.get('username')}
            return {"message": "Sesion iniciada","data":data_user}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
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
    # @classmethod
    # def edit_profile():
       
    #     username = session.get('username')
     
    #     user = User.get(User(username=username))
    #     if user is None:
    #         return {"message": "Usuario no encontrado"}, 404
    #     data = request.json  


    #     if 'nombre' in data:
    #         user.nombre = data['nombre']
    #     if 'apellido' in data:
    #         user.apellido = data['apellido']
    #     if 'email' in data:
    #         user.email = data['email']
    

    
    #     user.save()  

    #     return {"message": "Perfil actualizado exitosamente"}, 200





    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200