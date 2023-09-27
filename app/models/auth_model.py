from ..database import DatabaseConnection


class User:

    """ def __init__(self, user_id = None, username = None, password = None, email = None, first_name = None, last_name = None, date_of_birth = None, phone_number = None, creation_date = None, last_login = None, status_id = None, role_id = None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.creation_date = creation_date
        self.last_login = last_login
        self.status_id = status_id
        self.role_id = role_id """

    def __init__(self, **kwargs):   
        # self.id_user = kwargs.get('id_user')
        self.username = kwargs.get('username')
        self.password_username = kwargs.get('password_username')
        self.email = kwargs.get('email')
        self.profile_img = kwargs.get('profile_img')
        self.country = kwargs.get('country')  
        self.phone = kwargs.get('phone')
        self.birthdate = kwargs.get('birthdate')
    
    def serialize(self):
        return {
                    
            "username": self.username,
            "password_username": self.password_username,
            "email": self.email,
            "profile_img":self.profile_img,
            "country": self.country,
            "phone": self.phone,
            "birthdate": str(self.birthdate)                                    
        }
    @classmethod
    def create_user(cls, user):
        query = "INSERT INTO discord.user (username, password_username, email, profile_img, country, phone, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        params = user.username, user.password_username, user.email, user.profile_img, user.country, user.phone, user.birthdate
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def is_registered(cls,user):
        
            query = """SELECT * FROM discord.user 
                    WHERE username = %(username)s AND password_username = %(password)s"""
        
            params = {
                'username': user.username,
                'password': user.password_username
            }
            result = DatabaseConnection.fetch_one(query, params=params)
            
            if result is not None:
                user_data = {
                'id_user': result[0],
                'username': result[1],
                'email': result[2],
                'country': result[3],
                'phone': result[4],
                'birthdate': result[5]
                # Agrega todos los demás campos que desees recuperar aquí
                }
                return user_data
            else:return None
        
    @classmethod
    def confirmed_username(cls,user):
        query = """SELECT username FROM discord.user 
                WHERE username = %(username)s"""
        
        params = {
            'username': user.username,
            'password': user.password_username
        }
        result = DatabaseConnection.fetch_one(query, params=params)
       
        if result is not None:
            confirm_data = str(result[0])
            return confirm_data
        else: return False    
    
    @classmethod
    def arre(cls, user):
        try:
            query = """SELECT * FROM discord.user 
            WHERE username = %(username)s"""
        
            params = user.__dict__
            result = DatabaseConnection.fetch_one(query, params=params)
            if result is not None:
            
                return cls(
                    
                    username = result[1],
                    id_user = result[0],                
                    password_username = result[2],
                    email = result[3],
                    profile_img = result[4],
                    country = result[5],
                    phone = result[6],
                    birthdate = result[7]                             
                )
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la consulta
            print(f'Ocurrió un error: {str(e)}')
    @classmethod       
    def actualizar(cls,user1,user):
        
        # print("->",type(user1))
        usuario= User.arre(user1)
        # print("desde modelo..metodo actualizar-->",usuario)
        print(usuario.serialize())
        if usuario is not None:
            #actualizamos datos
            query="UPDATE discord.user SET "
            if user.email!=None:
                consulta=query + "email=%s WHERE username=%s"
                params= user.email, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.username!=None:
                consulta=query + "username=%s WHERE username=%s"
                params= user.username, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.phone!=None:
                consulta=query + "phone=%s WHERE username=%s"
                params= user.phone, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.country!=None:
                consulta=query + "country=%s WHERE username=%s"
                params= user.country, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.password_username!=None:
                consulta=query + "password_username=%s WHERE username=%s"
                params= user.password_username, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)    
            if user.birthdate!=None:
                consulta=query + "birthdate=%s WHERE username=%s"
                params= user.birthdate, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)

            return {"message":f"Los datos del usuario {user1.username} fueron modificados con exito"},200
        else:
            return {"message":"usuario no encontrado"}
    @classmethod
    def update(cls, user,id_user):
    
        query_parts = []
        params = []

        for key, value in user.items():
            query_parts.append(f"{key} = %s")
            params.append(value)

        
        params.append(id_user)  
        print(f"aca las querys{query_parts}")
        print(params)
       
        query = "UPDATE discord.user SET " + ", ".join(query_parts) + " WHERE id_user = %s"
        print(f"esta es la query{query}")
       
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update_password(cls, new_password, id_user): 
        query = "UPDATE discord.user SET password_user = %s WHERE id_user = %s"

        params =  new_password,id_user
        print(params)
        DatabaseConnection.execute_query(query, params)