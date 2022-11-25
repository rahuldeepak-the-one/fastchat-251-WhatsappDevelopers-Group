#
# Fast Chat


1. Group Name : Whatsapp Developer(RPR)
2. Group Memebers:
    1. Rahul deepak (21005090)
    2. Ravi Shankar Meena (210050135)
    3. Pragnan Maharshi (210050130)

#
# Information
 Fast Chat is a  network of clients interacting with each other with the help of some servers acting as mediators.
These packages are required for to run the program 
1. postgresql
2. socket
3. threading
4. sys
5. pickle
6. makepass
7. cryptography 
8. os 
9. threading
10. base64 
11. psycopg2
#
# Instructions
 Run client.py to connect with  the server and server asks for the username regardless of the user status being registered or not , after entering the username the functions checks for the username in the database if the username exist then password is asked if not then sign up is implemented
## commands 
1. @logout 
2. @get_all_members
3. @get_admins
4. @get_online_members
5. @kick_members

These are the commands for a group chat

#
# Data Base
1. Psotgresql is used for data basing for Storing client usernames, passwords and  key .
2.  different tables are created  for different groups which consists of members of the group and also for storing messages if the user is offline else it is immendiately sent and different functions are created addressing this 

#
# Server
 Server is the mediator for the communication between the clients . Running the client.py connects the server and client . server handles all the client requests through extensive functional programming and messages are encrypted while storing and sending the users 
 







  

