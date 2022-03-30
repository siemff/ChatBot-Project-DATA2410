"""
this Message class contains function attributs
which will be sent to clients as well as server.
"""
class Message:
    def __init__(self, sender: None, response=None, action=None, suggestion_type=None):
        self.sender = sender
        self.response = response
        self.action = action
        self.suggestion_type = suggestion_type

    def __str__(self):
        return self.sender, self.response, self.action, self.suggestion_type

class Client:
    def __init__(self, name=None, address=None, connection=None):
        self.name = name
        self.address = address
        self.connection = connection

    def __str__(self):
        return self.name, self.address, self.connection
