from ..models.server_model import Server

from flask import request

class ServerController:
    """Server controller class"""

    @classmethod
    def get(cls, id_server):
        """Get a server by id"""
        server = Server(id_server = id_server)
        result = Server.get(server)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Get all servers"""
        server_objects = Server.get_all()
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200
    
    @classmethod
    def create(cls):
        """Create a new server"""
        data = request.json
        print(f'Estoy recibiendo: {data}')
        # TODO: Validate data
        
        server = Server(**data)
        print(server)
        Server.create(server)
        return {'message': 'Server created successfully'}, 201

    @classmethod
    def update(cls, id_server):
        """Update a server"""
        data = request.json
        # TODO: Validate data
        
        data['id_server'] = id_server

        server = Server(**data)

        # TODO: Validate film exists
        Server.update(server)
        return {'message': 'Server updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_server):
        """Delete a server"""
        server = Server(id_server = id_server)

        # TODO: Validate server exists
        Server.delete(server)
        return {'message': 'Server deleted successfully'}, 204