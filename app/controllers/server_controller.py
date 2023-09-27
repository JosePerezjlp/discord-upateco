from ..models.server_model import Server
from ..models.exceptions import ServerNotFound
from ..models.auth_model import User
from ..models.channel_model import Channel
from flask import request, session

class ServerController:
    """Server controller class"""

    @classmethod
    def get(cls,id_server):    
        print(id_server)
        id_user = session.get('id_user')
        
        result = Channel.get_cs(id_user,id_server)
        if result is not None:
            return {"message":"channels encontrador","data":result}, 200
        else:
            raise ServerNotFound(id_server) 
                 
        
    @classmethod
    def get_all(cls):
        """Get all servers"""
        id_user = session.get('id_user')
        print(id_user)
        server_objects = Server.get_all(id_user)
        print(f"este es controller {server_objects}")
        servers = []       

        if server_objects is not None:
            for server in server_objects:
           
                servers.append(server)
            return {'message':"funciona","data":servers}, 200
        else: return {'message':"no se encontro nada"},400    

    @classmethod
    def create(cls):
        """Create a new server"""
        data = request.json
        
        id_user = session.get('id_user')
       
        # print(f'Acá tengo el id: {id_user}')
        
        # TODO: Validate data
        
        server = Server(**data)
        
        info_server = Server.create(server)
        if info_server is not None:
            session['id_server'] = info_server
            Server.create_UserServer(id_user)    
            return {}, 201
        else:return {"message":"no paso nada"}
        
        

    @classmethod
    def update(cls, id_server):
        """Update a server"""
        data = request.json
        # TODO: Validate data
        
        data['id_server'] = id_server

        server = Server(**data)
        
        if not server.exists(id_server):
            raise ServerNotFound(id_server)
        else:
            Server.update(server)
            return {'message': 'Server updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_server):
        """Delete a server"""
        server = Server(id_server = id_server)
        
        if not server.exists(id_server):
            raise ServerNotFound(id_server)
        else:
            Server.delete(server)
            return {'message': 'Server deleted successfully'}, 204