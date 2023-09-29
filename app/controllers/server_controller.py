from ..models.server_model import Server
<<<<<<< HEAD
from ..models.exceptions import ServerNotFound
from ..models.auth_model import User
from ..models.channel_model import Channel
from flask import request, session
=======

from flask import request
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155

class ServerController:
    """Server controller class"""

    @classmethod
<<<<<<< HEAD
    def get(cls,id_server):    
        print(id_server)
        id_user = session.get('id_user')
        
        result = Channel.get_cs(id_user,id_server)
        if result is not None:
            return {"message":"channels encontrador","data":result}, 200
        else:
            raise ServerNotFound(id_server)                  
=======
    def get(cls, id_server):
        """Get a server by id"""
        server = Server(id_server = id_server)
        result = Server.get(server)
        if result is not None:
            return result.serialize(), 200
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
        
    @classmethod
    def get_all(cls):
        """Get all servers"""
<<<<<<< HEAD
        id_user = session.get('id_user')
        # print(id_user)
        server_objects = Server.get_all(id_user)
        # print(f"este es controller {server_objects}")
        servers = []       

        if server_objects is not None:
           
            return {'message':"funciona","data":server_objects}, 200
        else: return {'message':"no se encontro nada"},400 


=======
        server_objects = Server.get_all()
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200
    
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
    @classmethod
    def create(cls):
        """Create a new server"""
        data = request.json
<<<<<<< HEAD
        
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
        
        
=======
        print(f'Estoy recibiendo: {data}')
        # TODO: Validate data
        
        server = Server(**data)
        print(server)
        Server.create(server)
        return {'message': 'Server created successfully'}, 201
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155

    @classmethod
    def update(cls, id_server):
        """Update a server"""
        data = request.json
        # TODO: Validate data
        
        data['id_server'] = id_server

        server = Server(**data)
<<<<<<< HEAD
        
        if not server.exists(id_server):
            raise ServerNotFound(id_server)
        else:
            Server.update(server)
            return {'message': 'Server updated successfully'}, 200
=======

        # TODO: Validate film exists
        Server.update(server)
        return {'message': 'Server updated successfully'}, 200
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
    
    @classmethod
    def delete(cls, id_server):
        """Delete a server"""
        server = Server(id_server = id_server)
<<<<<<< HEAD
        
        if not server.exists(id_server):
            raise ServerNotFound(id_server)
        else:
            Server.delete(server)
            return {'message': 'Server deleted successfully'}, 204
=======

        # TODO: Validate server exists
        Server.delete(server)
        return {'message': 'Server deleted successfully'}, 204
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
