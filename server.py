'Chat Room Connection - Client-To-Client'
import threading
import socket
import pickle
from database import *

host = 'localhost'
print ("Enter the port number -->>")
port = int(input())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
members = []
admins =[]

#  send message to all the clients in the group
def broadcast(message):
    ''' broadcasts the messages sent by a member to all other members in a group
    : param message: Takes input of the msg sent by client
    : type message : str
    '''
    for client in clients:
        client.send(message)

# Function to handle clients'connections
        
    
def handle_client(client):
    ''' handle a client and basing on the msg, executes different commands
    : param client :socket of the client
    : type client : socket
    '''
    while True:
        try:
            msg = client.recv(1024)
            if msg == "@kick_member" :
                if client in admins:
                    client.send(b"type username of the person to kick him out")
                    kick_member = client.receive(1024).decode('utf-8')
                    if check_user(kick_member) == True:
                        clients.remove(kick_member)
                        members.remove(kick_member)
                        broadcast(f'{kick_member} has kicked out of the group'.encode('utf-8'))
                    else :
                        client.send(b"there is no person with this username")
                else:
                    client.send(b"You aren't an admin")             
            elif msg == "@get_admins":
                k = str(admins)
                k = k.encode()
                client.send(k)
            elif msg == "@get_online_members":
                k = str(clients)
                k = k.encode()
                client.send(k)
            elif msg == "@get_all_members":
                k = str(members)
                k = k.encode()
                client.send(k)
            elif msg == "LOGOUT":
                clients.remove(client)
                client.close()
                broadcast(f'{client} has left group'.encode('utf-8'))
            # elif msg == "SENDMSG":
            #     # msg =pickle.loads(msg)[1]
            #     # name2 = client.recv(1024).decode('utf-8')
            #     # for name in clients:
            #     #     if name == name2:
            #     #         name2.send(msg)
            else:
                broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = members[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            print("f'{alias} has left the chat room!'")            
            members.remove(alias)
            break
        
# Main function to receive the clients connection
def receive():
    '''receives the connection from client and connects to server
        starts the thread from client to
    '''
    while True: 
        print('Server is ready to use ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        members.append(alias)
        clients.append(client)
        print(f'The new member of this chatroom is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send("' you are now connected !'".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
