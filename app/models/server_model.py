from ..database import DatabaseConnection
<<<<<<< HEAD
from .channel_model import Channel
=======
from .exceptions import DatabaseError, ServerNotFound
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
class Server:
    """Server model class"""

    def __init__(self, id_server = None, servername = None, description_server = None, creation_date = None):
        """Constructor method"""
        self.id_server = id_server
        self.servername = servername
        self.description_server = description_server
        self.creation_date = creation_date

    def serialize(self):
<<<<<<< HEAD
      
=======
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:
            - The last_update attribute is converted to string
            - The special_features attribute is converted to list if it is not
            null in the database. Otherwise, it is converted to None
            - The attributes rental_rate and replacement_cost are converted to 
            int, because the Decimal type may lose precision if we convert 
            it to float
        """
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
        return {
            "id_server": self.id_server,
            "servername": self.servername,
            "description_server": self.description_server,
            "creation_date": str(self.creation_date)
        }
<<<<<<< HEAD
   
    @classmethod
    def get(cls,id_user,id_server):
        info = Channel.get_cs(id_user,id_server) 
        print(f"{info}") 
        # try:
        #     query = """SELECT id_server, servername, description_server, creation_date FROM discord.server WHERE id_server = %s"""
        #     params = idserver.id_server,
        #     result = DatabaseConnection.fetch_one(query, params=params)

        #     if result is not None:
        #         return cls(*result)
        # except Exception as e:
        # # Manejar cualquier excepción que pueda ocurrir durante la consulta
        #     print(f'Ocurrió un error: {str(e)}')       
    
    @classmethod
    def get_all(cls, id_user):
        try:
                params = (id_user,)
                query = "SELECT DISTINCT u.id_user, u.username, s.id_server, s.servername FROM discord.user_server us INNER JOIN discord.user u ON us.id_user = u.id_user INNER JOIN discord.server s ON s.id_server = us.id_server WHERE u.id_user = %s;"

                with DatabaseConnection.get_connection() as connection:
                    cursor = connection.cursor()
                    cursor.execute(query, params)
                    results = cursor.fetchall()
                    

                servers = []
                if results:
                    for result in results:
                       
                        server = cls(*result)
                        ref = server.serialize()
                        servers.append(ref)

                return servers
        except Exception as e:
                return (f'{str(e)}')
    # @classmethod
    # def get_all(cls,id_user):
    #     """Get all servers
    #     Returns:
    #         - list: List of Server objects
    #     """
            
    #     try:
    #         params = id_user,
    #         print(params)
    #         query = """SELECT DISTINCT u.id_user, u.username, s.id_server, s.servername
    #                     FROM discord.user_server us
    #                     INNER JOIN discord.user u ON us.id_user = u.id_user
    #                     INNER JOIN discord.server s ON s.id_server = us.id_server 
    #                     WHERE u.id_user = %s;"""
    #         results = DatabaseConnection.fetch_all(query,params=params)
            
    #         # servers = []
    #         if results is not None:
    #             print(results)
    #             # for result in results:
    #             #     servers.append(cls(*result))

            
    #         return results
    #     except Exception as e:
    #     # Manejar cualquier excepción que pueda ocurrir durante la consulta
    #         print(f'Ocurrió un error: {str(e)}')       

=======
    
    @classmethod
    def get(cls, server):
        """Get a server by id
        Args:
            - server (Server): Server object with the id attribute
        Returns:
            - Server: Server object
        """
        query = """SELECT id_server, servername, description_server, creation_date FROM discord.server WHERE id_server = %s"""
        params = server.id_server,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        else:
            raise ServerNotFound("El server solicitado no existe")
    
    @classmethod
    def get_all(cls):
        """Get all servers
        Returns:
            - list: List of Server objects
        """
        query = """SELECT id_server, servername, description_server, creation_date FROM discord.server"""
        results = DatabaseConnection.fetch_all(query)
        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
    
    @classmethod
    def create(cls, server):
        """Create a new server
        Args:
            - server (Server): Server object
        """
        #print(f'En el server tengo: {server}')
<<<<<<< HEAD
       
        #print(f'Aca tengo: {server.servername}')
        #print(f'Por aca tengo: {server.description_server}')
        
        query = """INSERT INTO discord.server (servername, description_server) VALUES (%s, %s)"""
        params = server.servername, server.description_server
        cursor = DatabaseConnection.execute_query(query, params=params)
        if cursor is not None:
            inserted_id = cursor.lastrowid
            return inserted_id
        else: return None 
        
    @classmethod
    def create_UserServer(cls, id_user):
        try:
            query = """INSERT INTO discord.user_server(id_server, id_user) VALUES ((SELECT MAX(server.id_server) FROM discord.server),  %s);"""
            print(id_user)
            params = id_user,
            DatabaseConnection.execute_query(query, params=params)
            return {"message": "Servidor Registrado con exito!"}, 201
        except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la consulta
            print(f'Ocurrió un error: {str(e)}')
    @classmethod
=======
        query = """INSERT INTO discord.server (servername, description_server) VALUES (%s, %s)"""
        params = server.servername, server.description_server
        #print(f'Aca tengo: {server.servername}')
        #print(f'Por aca tengo: {server.description_server}')
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1:
            id_server = cursor.lastrowid
            return id_server
        else:
            raise DatabaseError("No se pudo crear el server nuevo ")
        
    @classmethod
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
    def update(cls, server):
        """Update a server
        Args:
            - server (Server): Server object
        """
        params = server.servername, server.description_server, server.id_server
        query = "UPDATE discord.server SET server.servername = %s, server.description_server = %s WHERE id_server = %s"
<<<<<<< HEAD
        DatabaseConnection.execute_query(query, params=params)
        
        # if cursor.rowcount == 1:
        #     id_server = cursor.lastrowid
        #     return id_server
        # else:
        #     raise DatabaseError("No se pudo actualizar el server")
=======
        
        cursor = DatabaseConnection.execute_query(query, params=params)
        
        if cursor.rowcount == 1:
            id_server = cursor.lastrowid
            return id_server
        else:
            raise DatabaseError("No se pudo actualizar el server")
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
    
    @classmethod
    def delete(cls, server):
        """Delete a server
        Args:
            - server (Server): Server object with the id attribute
        """
        query = "DELETE FROM discord.server WHERE id_server = %s"
        params = server.id_server,
<<<<<<< HEAD
        DatabaseConnection.execute_query(query, params=params)
        
        # if cursor.rowcount == 0:
        #     raise DatabaseError("No se pudo eliminar el server")
        # else:
        #     return {"message": "Server eliminado con exito"}
    
    @classmethod   
    def exists(cls, server):
        try:
            query = "SELECT COUNT(*) FROM discord.server WHERE id_server = %s"
            params = (server,)
            result = DatabaseConnection.fetch_one(query, params=params)
            return result[0] > 0
        except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la consulta
            print(f'Ocurrió un error: {str(e)}')
=======
        cursor = DatabaseConnection.execute_query(query, params=params)
        
        if cursor.rowcount == 0:
            raise DatabaseError("No se pudo eliminar el server")
        else:
            return {"message": "Server eliminado con exito"}
>>>>>>> b9601805bb5366600b82baf2877761dcb46a3155
