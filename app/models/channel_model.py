from ..database import DatabaseConnection

class Channel:
    """Channel model class"""

    def __init__(self, id_channel = None, chaneel_name = None, description_channel = None, id_server = None):
        """Constructor method"""
        self.id_channel = id_channel
        self.chaneel_name = chaneel_name
        self.description_channel = description_channel
        self.id_server = id_server

    def serialize(self):
       
        return {
            "id_channel": self.id_channel,
            "chaneel_name": self.chaneel_name,
            "description_channel": self.description_channel,
            "id_server": self.id_server
        }
        
    @classmethod
    def get_cs(cls, id_user, id_server):
        
        query = "SELECT c.id_channel,c.chaneel_name,c.description_channel,s.id_server FROM discord.channel c INNER JOIN discord.user_server us ON c.id_server = us.id_server INNER JOIN discord.user u ON us.id_user = u.id_user INNER JOIN discord.server s ON s.id_server = c.id_server WHERE u.id_user = %s and s.id_server= %s;"
                
        params = id_user, id_server 
        results = DatabaseConnection.fetch_all(query, params=params)
        print(results)
        channels = []
        if results is not None:
            for result in results:
                cls={
                    "id_channel": result[0],
                    "chaneel_name": result[1],
                    "description_channel": result[2],
                    "id_server": result[3]
                }
                channels.append(cls)
            return channels
        else: return None
        
    
    @classmethod
    def get(cls, channel):
        
        query = """SELECT id_channel, chaneel_name, description_channel, id_server FROM discord.channel WHERE id_channel = %s"""
        params = channel.id_channel,
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return cls(*result)
        else:
            return None

    
    @classmethod
    def get_all(cls):
       
        query = """SELECT id_channel, chaneel_name, description_channel, id_server FROM discord.channel"""
        results = DatabaseConnection.fetch_all(query)
        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(*result))
                
        return channels
    
    
    @classmethod
    def create(cls, channel):
       
        query = """INSERT INTO discord.channel (chaneel_name, description_channel, id_server) VALUES (%s, %s, %s)"""
        params = channel.chaneel_name, channel.description_channel, channel.id_server
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, channel):
        params = channel.chaneel_name, channel.description_channel, channel.id_channel
        query = "UPDATE discord.channel SET channel.chaneel_name = %s, channel.description_channel = %s WHERE id_channel = %s"
        
        DatabaseConnection.execute_query(query, params=params)
        
    @classmethod
    def delete(cls, channel):
        
        query = "DELETE FROM discord.channel WHERE id_channel = %s"
        params = channel.id_channel,
        DatabaseConnection.execute_query(query, params=params)
        

    @classmethod   
    def exists(cls, channel):
        query = "SELECT COUNT(*) FROM discord.channel WHERE id_channel = %s"
        params = (channel,)
        result = DatabaseConnection.fetch_one(query, params=params)
        return result[0] > 0
    
    @classmethod
    def get_all_channel(cls, id_user, id_server):
        query = """SELECT u.id_user, u.username, s.id_server, s.servername, c.chaneel_name
                    FROM discord.channel c
                    INNER JOIN discord.user_server us ON c.id_server = us.id_server
                    INNER JOIN discord.user u ON us.id_user = u.id_user
                    INNER JOIN discord.server s ON s.id_server = c.id_server 
                    WHERE u.id_user = %s and s.id_server= %s;"""
        params = results = DatabaseConnection.fetch_all(query)
        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(*result))
        return channels