#!/usr/bin/env python
import socket
import pickle
import random
import threading
import time

from bots_setup.bots import choose_bot
from bots_setup.communication import Message

# Connection (to server)
IPADDR = '127.10.10.10'
PORT = 8080
ADDRESS = (IPADDR, PORT)

# Bots name to identify the Clien
bots = ("Madelen", "Felix", "Marija", "Rateb")
USERNAME = random.choice(bots)

# Connection:
# contains messages from host and responses from bots
get_server_messages = []
get_bot_responses = []

# functions that recives messages from server as well as bots
# and makes sure that 4 responses from all clients/bots are recived by creating array
def msg_fromServer(connection: socket):
    while True:
        try:
            msg_received = connection.recv(1024)  # receive as long as message strings are not empty
            if msg_received:
                msg: Message = pickle.loads(msg_received)  # deserialize byte stream to python object
            else:
                continue
            if msg.sender == 'Host':
                if msg.response == 'USERNAME':
                    random_usr = Message(sender=USERNAME)  # serialize Usernames into byte stream
                    connection.send(pickle.dumps(random_usr))
                else:
                    get_server_messages.append(msg)  # appends message from host to be added in the list
                    print(f"{msg.sender}: {msg.response}")  # Message from host, suggesting...
            else:
                get_bot_responses.append(msg)  # appends replays from bots to be added in list
                time.sleep(2)  # suspends executaion of the thread for 2s
                print(f"{msg.sender}: {msg.response}")  # Message from bots

            if len(get_bot_responses) == 4:  # When all clients have responded the connection ends
                disconnect = Message(sender=USERNAME, response="Bye")
                connection.send(pickle.dumps(disconnect))
                break
        except OSError as e:
            print(e)
            break
    connection.close()

# function that imports bots responses by using choose_bot function
# which contains the attributes: bot name and response
def w_msg(connection: socket):
    while True:
        if len(get_server_messages) == 1:
            msg = choose_bot(USERNAME, get_server_messages[0])
            pickle_msg = pickle.dumps(msg)
            connection.send(pickle_msg)
            break
        else:
            continue

if __name__ == "__main__":
    try:
        # create a socket at server side using TCP/IP protocol
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # initiates TCP server connection
        client.connect(ADDRESS)
        # object of Thread class to creat thread.
        # target: the fuction to be executed by thread
        # args: the aruments to be passed to the target fuction
        receive_thread = threading.Thread(target=msg_fromServer, args=(client,))  # Creating new thread
        receive_thread.start()  # starting thread
        write_thread = threading.Thread(target=w_msg, args=(client,))  # Creating thread
        write_thread.start()  # Creating thread
    except ConnectionRefusedError:
        print(f"You can't connect to the chatroom.\n No server is bind to address:{ADDRESS} not running")
