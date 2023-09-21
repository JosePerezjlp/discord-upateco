# from ..database import DatabaseConnection


# class User:

#     """ def __init__(self, user_id = None, username = None, password = None, email = None, first_name = None, last_name = None, date_of_birth = None, phone_number = None, creation_date = None, last_login = None, status_id = None, role_id = None):
#         self.user_id = user_id
#         self.username = username
#         self.password = password
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.phone_number = phone_number
#         self.creation_date = creation_date
#         self.last_login = last_login
#         self.status_id = status_id
#         self.role_id = role_id """

#     def __init__(self, **kwargs):
#         self.user_id = kwargs.get('user_id')
#         self.username = kwargs.get('username')
#         self.password_username = kwargs.get('password_username')
#         self.email = kwargs.get('email')
#         self.first_name = kwargs.get('first_name')
#         self.last_name = kwargs.get('last_name')
#         self.date_of_birth = kwargs.get('date_of_birth')
#         self.phone_number = kwargs.get('phone_number')
#         self.creation_date = kwargs.get('creation_date')
#         self.last_login = kwargs.get('last_login')
#         self.status_id = kwargs.get('status_id')
#         self.role_id = kwargs.get('role_id')
    
#     def serialize(self):
#         return {
#             "user_id": self.user_id,
#             "username": self.username,
#             "password_username": self.password_username,
#             "email": self.email,
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "date_of_birth": self.date_of_birth,
#             "phone_number": self.phone_number,
#             "creation_date": self.creation_date,
#             "last_login": self.last_login,        
#         }

#     @classmethod
#     def create_user(cls, user):
#         query = "INSERT INTO discord.user (id_user, username, password_username, email,profile_img, country,phone, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
#         params = user
#         DatabaseConnection.execute_query(query, params)