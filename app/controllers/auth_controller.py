from ..models.auth_model import User

from flask import request, session,jsonify

class AuthController:

    @classmethod
    def login(cls):
        data = request.json 
        user = User(**data)        
        exist = User.is_registered(user)   
        
        if exist is not None:
           
            session['username'] = data.get('username')
            session['id_user'] = exist.get('id_user')
          
            data_user = {"id":exist,"username":data.get('username')}
            return {"message": "Sesion iniciada","data":data_user}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    @classmethod
    def register(cls):
       
        data = request.json
        print(f'Estoy recibiendo: {data}')        
        user = User(**data)
        
        confirm = User.confirmed_username(user)       
        if confirm != data.get('username'):
            User.create_user(user)
            return {'message': 'Cuenta creada con exito'}, 201
        else : return {'message': 'El nombre de usuario esta en uso'}, 400

    @classmethod
    def show_profile(cls):
        username = session.get("username")
       
        user = User.arre(User(username = username))       
        if user is not None:
            
            return user.serialize(), 200
            
        else:
            return {"message": "Usuario no encontrado"}, 404
   
            
    @classmethod
    def actualizar(cls):
        data = request.json
        user1=User(username=session.get('username'))
        print(user1.serialize())
        """actualizar por el nombre de usuario"""
        
        email= request.args.get("email")
        name_usuario= request.args.get("username")
        phone = request.args.get('phone')
        country = data.get('country')
        
        password_username= data.get("password_username")
        birthdate= request.args.get("birthdate")
        # print(birthdate)        

        user=User(username=name_usuario,email=email,password_username=password_username,birthdate=birthdate,phone=phone,country=country)

        return User.actualizar(user1,user)
     
    # @classmethod
    # def edit_profile(cls):
    #     data = request.json        
    #     username = session.get('username')          
    #     user = User.arre(User(username=username))
        
    #     id_user = session.get('id_user')
    #     if user is None:
    #         return {"message": "Usuario no encontrado"}, 404
    #     if 'email' in data:
    #         user.email = data['email']            
    #     if 'country' in data:
    #      user.country = data['country']
    #     if 'phone' in data:
    #      user.phone = data['phone']
    #     if 'birthdate' in data:
    #         user.birthdate = data['birthdate']
    #         user.profile_img = 'asd'    
    #     User.update(user.serialize(),id_user)        
    #     return jsonify({"message": "Perfil actualizado exitosamente"}), 200
    
    @classmethod
    def change_password(cls):
        data = request.json
        id_user = session.get('id_user')
        username = session.get('username')
        user = User.arre(User(username=username))    
       
        if user is None:
            return {"message": "Usuario no encontrado"}, 404

        else:
             
             User.update_password(data.get('password_username'), id_user)

             return jsonify({"message": "Contraseña actualizada exitosamente"}), 200

    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200