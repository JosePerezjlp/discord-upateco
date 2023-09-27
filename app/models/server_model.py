from ..database import DatabaseConnection
class Server:
    """Server model class"""

    def __init__(self, id_server = None, servername = None, description_server = None, creation_date = None):
        """Constructor method"""
        self.id_server = id_server
        self.servername = servername
        self.description_server = description_server
        self.creation_date = creation_date

    def serialize(self):
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
        return {
            "id_server": self.id_server,
            "servername": self.servername,
            "description_server": self.description_server,
            "creation_date": str(self.creation_date)
        }
    
    @classmethod
    def get(cls, server):
        """Get a server by id
        Args:
            - server (Server): Server object with the id attribute
        Returns:
            - Server: Server object
        """
        try:
            query = """SELECT id_server, servername, description_server, creation_date FROM discord.server WHERE id_server = %s"""
            params = server.id_server,
            result = DatabaseConnection.fetch_one(query, params=params)

            if result is not None:
                return cls(*result)
        except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la consulta
            print(f'Ocurrió un error: {str(e)}')       
    
    @classmethod
    def get_all(cls, id_user):
        # try:
            params = (id_user,)
            print(params)
            query = """SELECT DISTINCT u.id_user, u.username, s.id_server, s.servername
                        FROM discord.user_server us
                        INNER JOIN discord.user u ON us.id_user = u.id_user
                        INNER JOIN discord.server s ON s.id_server = us.id_server 
                        WHERE u.id_user = %s;"""
            results = DatabaseConnection.fetch_all(query, params=params)

            servers = []
            if results is not None:
                for result in results:
                    # Crear objetos Server a partir de los resultados y agregarlos a la lista servers
                    server = cls(*result)
                    servers.append(server)
                print(servers)
                return servers
        # except Exception as e:
        #     # Manejar cualquier excepción que pueda ocurrir durante la consulta
        #     print(f'Ocurrió un error: {str(e)}')
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

    
    @classmethod
    def create(cls, server):
        """Create a new server
        Args:
            - server (Server): Server object
        """
        #print(f'En el server tengo: {server}')
       
        #print(f'Aca tengo: {server.servername}')
        #print(f'Por aca tengo: {server.description_server}')
        try:
            query = """INSERT INTO discord.server (servername, description_server) VALUES (%s, %s)"""
            params = server.servername, server.description_server
            cursor = DatabaseConnection.execute_query(query, params=params)
            inserted_id = cursor.lastrowid
            return inserted_id
        except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la consulta
            print(f'Ocurrió un error: {str(e)}')       

        
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
    def update(cls, server):
        """Update a server
        Args:
            - server (Server): Server object
        """
        params = server.servername, server.description_server, server.id_server
        query = "UPDATE discord.server SET server.servername = %s, server.description_server = %s WHERE id_server = %s"
        DatabaseConnection.execute_query(query, params=params)
        
        # if cursor.rowcount == 1:
        #     id_server = cursor.lastrowid
        #     return id_server
        # else:
        #     raise DatabaseError("No se pudo actualizar el server")
    
    @classmethod
    def delete(cls, server):
        """Delete a server
        Args:
            - server (Server): Server object with the id attribute
        """
        query = "DELETE FROM discord.server WHERE id_server = %s"
        params = server.id_server,
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