import threading
import sys
import pickle
import socket
import maskpass
from database import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("### Enter the port number ###")
port = int(input())

try:
    client.connect(('localhost', port))   
except Exception as e:
    logging.exception("there is no server present with port number " + port)   
 
alias = input('### Enter your Username ###')
if check_user(alias) == True:
    print("#### Good to see you again " + alias + "!" )
    print("#### Enter your password to join the chat :")
    while True:
        password = maskpass.askpass(prompt="Password:",mask = " ")
        if password == "@exit":
            sys.exit()
        if check_password(alias ,password) == False:
            print("***Please try again ! ***")
            print("*** type @exit to quit ***")
        else:
            print("*** welcome back "+ alias + "! ***") 
            break   
else:
    print("### Type in a password for your new account :")
    password = input()
    insert_user(alias ,password)
    print("*** successfully created your account ***")

if total_mem() == 0:
    print("### To create a new group enter its Name : ")
    groupname = input()
    print("###" + groupname +"is successfully created")
else:
    print("### joining into the group ....")

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            logging.exception("Error!", e)
            client.close()
            break


def client_send():
    '''
    receives the input from terminal and sends it to the terminal
    '''
    while True:
        try:
            msg =input()
            if msg == "LOGOUT":
                sys.exit()
            elif msg == "@kick_member":
                client.send(bytes(".","utf-8"))
                name = input()
                client.send(bytes(name,"utf-8"))
                print(client.recv().decode("utf-8"))
            elif msg == "@get_admins":
                client.send(bytes(".","utf-8"))
                list = pickle.loads(client.recv(2048)).decode('utf-8')
                print("members of this group are :")
                for i in range(len(list)):
                    print(list[i] + " ")
            elif msg == "@get_all_members":
                client.send(bytes(".","utf-8"))
                list = pickle.loads(client.recv(2048)).decode('utf-8')
                print("members of this group are :")
                for i in range(len(list)):
                    print(list[i] + " ")
            elif msg == "@get_online_members":
                client.send(bytes(".","utf-8"))
                list = pickle.loads(client.recv(2048)).decode('utf-8')
                print("members of this group are :")
                for i in range(len(list)):
                    print(list[i] + " ")
            elif msg == "SENDMSG":
                print("to whom do you need to send the message :")
                rcvr = str(input())
                client.send(rcvr.encode('utf-8'))
                print("enter the message :")
                msg = str(input())
                client.send(msg.encode('utf-8'))
            else:
                message = f'{alias}: {msg}'
                client.send(message.encode('utf-8'))
                # tuple = (rcvr)
                # tuple = pickle.dumps(tuple)
                # client.send(tuple)
                # while True:
                #         print("type EXIT to quit")
                #         while True:
                #             message = str(input())
                #             if message == "EXIT":
                #                 break
                #             elif message:
                #                 message = message.encode("utf-8")
                #                 message = (message, rcvr)
                #                 message = pickle.dumps(message)
                #                 client.send(message)
        except Exception:
            client.send(bytes("LOGOUT","utf-8"))
            sys.exit(1)


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
