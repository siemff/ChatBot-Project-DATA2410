"""
this Message class contains attributs for communication
between server and clients
"""
class Message:
    def __init__(self, sender: None, response=None, action=None, suggestion_type=None):
        self.sender = sender  # username
        self.response = response  # communicatoin between
        self.action = action  # action from bots
        self.suggestion_type = suggestion_type  # suggestion from bots

    def __str__(self):
        return self.sender, self.response, self.action, self.suggestion_type


"""
Method that takes in name, address and connection
so that the client can be assigned into the server.
"""
class Client:
    def __init__(self, name=None, address=None, connection=None):
        self.name = name
        self.address = address
        self.connection = connection

    def __str__(self):
        return self.name, self.address, self.connection
