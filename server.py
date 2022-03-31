#!/usr/bin/env python
import argparse
import socket
import threading
import time
import pickle

from bots_setup.communication import Message
from bots_setup.communication import Client
from bots_setup.bots import my_bot

# Connection
IPADDR = '127.10.10.10'
PORT = 8080
ADDRESS = (IPADDR, PORT)
# Clients that have been connected:
clients = {}
threads = {}
usrnames = []

def start_threads():                        #the client handler_threds will begin after connection loop
    for count in threads:
        threads[count].start()               # Make the new thread ready.
        time.sleep(2.5)                     # puts a thread to sleep for 2.0 seconds

def connection_msg(msg, clients):
    pickle_msg = pickle.dumps(msg)
    for client in clients:
        clients[client].connection.send(pickle_msg)

#This fuctions rec
def client_action(connection):
    while True:
        msg = connection.recv(1024)             #Recive message from server
        unpickle_msg = pickle.loads(msg)    #deserialize a byte stream into a python object
        if unpickle_msg.response == "Bye":
            client = clients.pop(unpickle_msg.sender)
            print(client.name, "left the chatroom.")
            time.sleep(5)                   #after 10s the server clothes the chatroom
            client.connection.close()
            threads.pop(unpickle_msg.sender)
            break
        else:
            connection_msg(unpickle_msg, clients)
            print(f"{unpickle_msg.sender}: {unpickle_msg.response}")

connection_bad = Message(sender="Host", response="The bot is already in the chat, please come back with another name")

def logg_msg():
    while True:
        c, addr = server_socket.accept()             #wait till a client accepts connection
        connected = Message(sender="Host", response="USERNAME")
        c.send(pickle.dumps(connected))              #send connection message to client, so we can receive bot_name
        username = pickle.loads(c.recv(1024)).sender #recive message string from server at time 1024 B

        if username not in usrnames:
            usrnames.append(username)
            person = Client(name=username, address=addr, connection=c)  # creating object of Person
            # sending the connection confirmation back to the client
            clients[username] = person
            # a print out message just for the server
            info = f"New connection from {person.address} "\
                   f"{person.name} has joined the chatroom"
            print(info)
            connection_ok = Message(sender="Host", response=f"Introducing our awesome bot {person.name}!."
                                                            f"\nWating for all clients to join the chat.")
            pickle_msg = pickle.dumps(connection_ok)
            person.connection.send(pickle_msg)                  # sending the connection confirmation back to the client
            thread = threading.Thread(target=client_action, args=(person.connection,))  # creating new thread for handling the client
            threads[username] = thread                              # adding the thread to a dictionary of threads
        else:
            print(f"Bot_name, {username}, is taken please try another bot_name.")
            c.send(pickle.dumps(connection_bad))
            usrnames.pop(usrnames.index(username))
            c.close()
        # if all the bots are connected, then the chat begins with a suggestion message from the server
        if len(clients) == 4:
            time.sleep(1)
            suggested_msg = my_bot()                # there is a simple bot function that decides the first message
            print(f"{suggested_msg.sender}: {suggested_msg.response}")
            connection_msg(suggested_msg, clients)   # sends the message to all the bots
            break
        else:
            print(f"Waiting for {4 - len(clients)} client(s) to join the chat.")  # not sure yet
            continue
    start_threads()  # starting the threads

if __name__ == "__main__":
    # create a socket at server side using TCP/IP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDRESS) # binding address (address and port number pait) to socket
    server_socket.listen(4)  # allow maximum 4 connection to the socket

    print(f"SERVER LISTENING on {ADDRESS} ...")
    logg_msg()  # executing the main function of the server
