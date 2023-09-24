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
        query = """SELECT id_user FROM discord.user 
                WHERE username = %(username)s AND password_username = %(password)s"""
        
        params = {
            'username': user.username,
            'password': user.password_username
        }
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is None:
            return False
        else: return result
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
    def get(cls, user):
        query = """SELECT * FROM discord.user 
        WHERE username = %(username)s AND password_username = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return cls(
                user_id = result[0],
                username = result[1],
                password_username = result[2],
                email = result[3],
                profile_img = result[4],
                country = result[5],
                phone = result[6],
                birthdate = result[7]                             
            )
        return None