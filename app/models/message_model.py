from ..database import DatabaseConnection
from .auth_model import User
from .exceptions import DatabaseError

class Message:
    """Clase que representa un mensaje."""
    
    def __init__(self, **kwargs):
        self.id_message = kwargs.get('id_message')
        self.content = kwargs.get('content')
        self.creation_message = kwargs.get('creation_message')
        self.id_user = kwargs.get('id_user')
        self.id_channel = kwargs.get('id_channel')
    
    def serialize(self):
        return {
            "id_message": self.id_message,
            "content": self.content,
            "creation_message": self.creation_message, 
            "id_user": self.id_user,
            "id_channel": self.id_channel
        }

    def serialize2(self):
        return {
            "id_message": self.id_message,
            "content": self.content,
            "creation_message": self.creation_message, 
            "id_user": User.arre(User(id_user=self.id_user)).serialize() if self.id_user else None,
            "id_channel": self.id_channel
        }

    @classmethod
    def get_messages(cls, id_channel):
        query = """SELECT content, creation_message, id_user, id_channel FROM discord.message WHERE id_channel= %s ORDER BY creation_message DESC;"""
    
        params = id_channel,
        results = DatabaseConnection.fetch_all(query, params=params)
        
        message_list = []
        for result in results:
            message_list.append(Message(
                id_message = result[0],
                content = result[1],
                creation_message = result[2],
                id_user = result[3],
                id_channel = result[4]
            ))
        return message_list

    @classmethod
    def create_message(cls, message):
        query = """INSERT INTO discord.message (content, id_user, id_channel)
                VALUES (%s, %s, %s)"""
        params = message.content, message.id_user, message.id_channel
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update_message(cls, message):
        pass

    @classmethod
    def delete_message(cls, message):
        query = """DELETE FROM discord.messages WHERE message_id = %s"""
        params = message.message_id,
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 0:
            raise DatabaseError("No se pudo eliminar al mensaje")
        else:
            return {"message": "Mensaje eliminado con exito"}