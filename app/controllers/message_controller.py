from ..models.message_model import Message
from flask import request

class MessageController:
    """Clase de controlador de mensajes."""

    @classmethod
    def get_message(self, id_message):
        return Message.get_message(Message(
            id_message = id_message
        )).serialize(), 200
    
    @classmethod
    def get_messages(cls,message_id):
        data = request.json
        print(data)
        # messages = []
        # if request.args.get('id_channel'):
        #     message_obj = Message(id_channel=request.args.get('id_channel'))
        #     print("MESSAGE OBJ:", message_obj.id_channel, message_obj.content, message_obj.id_channel)
        #     messages = Message.get_messages(message_obj)
        # else:
        #     print("SEGUNDO GET")
        #     messages = Message.get_messages()
        # return [message.serialize2() for message in messages], 200
        print(message_id)
        msj_objects = Message.get_messages(message_id)
        print(f"este es controller {msj_objects}")
        # servers = []
        # for server in server_objects:
        #     # servers.append(server.serialize())
        if msj_objects is not None:
            return {'message':"funciona"}, 200
        else: return {'message':"no se encontro nada"},400


    # @classmethod
    # def get_messages(self):
    #     print("LLEGO A GET_MESSAGES")
    #     message_objects = Message.get_messages()
    #     print("DESPUES DE GET_MESSAGES")
    #     messages = []
    #     for message in message_objects:
    #         messages.append(message.serialize())
    #     return messages, 200

    @classmethod
    def create_message(self):
        data = request.json
        print(f'La data es: {data}')
        message = Message(**data)
        Message.create_message(message)

        return {}, 201
    
    @classmethod
    def update_message(self, id_message):
        pass
    
    @classmethod
    def delete_message(self, id_message):
        message = Message(id_message_id=id_message)
        Message.delete_message(message)

        return {}, 200