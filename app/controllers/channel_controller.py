from ..models.channel_model import Channel
from ..models.server_model import Server
from ..models.exceptions import ChannelNotFound

from flask import request

class ChannelController:
    """Channel controller class"""

    @classmethod
    def get(cls, id_channel):
        """Get a channel by id"""
        channel = Channel(id_channel = id_channel)
        result = Channel.get(channel)
        if result is not None:
            return result.serialize(), 200
        else:
            raise ChannelNotFound(id_channel)
        
    @classmethod
    def get_cs(cls, id_server):
        """Get a channel by id_server and id_user"""
        channel = Channel(id_server = id_server)
        result = Channel.get_cs(channel)
        if result is not None:
            return result.serialize(), 200 
        
    @classmethod
    def get_all(cls):
        """Get all channels"""
        channel_objects = Channel.get_all()
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200
    
    @classmethod
    def create(cls):
        """Create a new channel"""
        data = request.json
        # print(f'Estoy recibiendo: {data}')
        # TODO: Validate data
        
        channel = Channel(**data)
        print(channel)
        Channel.create(channel)
        return {'message': 'Channel created successfully'}, 201

    @classmethod
    def update(cls, id_channel):
        """Update a channel"""
        data = request.json
        # TODO: Validate data
        
        data['id_channel'] = id_channel

        channel = Channel(**data)
        
        if not channel.exists(id_channel):
            raise ChannelNotFound(id)

        Channel.update(channel)
        return {'message': 'Channel updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_channel):
        """Delete a server"""
        channel = Channel(id_channel = id_channel)

        # TODO: Validate server exists
        Channel.delete(channel)
        return {'message': 'Server deleted successfully'}, 204