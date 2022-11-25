import psycopg2
import logging
from encryption import *

# check if there is a user with the given name
def check_user(name):
    '''
    checks the name of the user in databse and returns true if 
    user name is in databse else returns false
    
    :param name: name of the user
    :type name: string
    :rtype: bool
    '''
    connection = psycopg2.connect(
    host = '127.0.0.1',
    database = 'database',
    user = 'postgres',
    password = 'rahul11',
    port = '5432'
    )
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT name FROM user_info ''')
        users = cursor.fetchall()

        for user in users:
            if user[0] == name:   
                return True
        connection.commit()
        connection.close() 
        return False             
    except Exception as e:
        logging.exceptions(e)

   
# check wheteher the password is matching or not  
def check_password(name , password):
    '''
    checks if the password matches to the actual password in database
    :param name: name of the user
    :type name: string
    :param password: password
    :type password: string
    :rtype: bool
    '''
    connection = psycopg2.connect(
    host = '127.0.0.1',
    database = 'database',
    user = 'postgres',
    password = 'rahul11',
    port = '5432'
    )
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM user_info ''')
        users = cursor.fetchall()

        for user in users:
            if user[0] == name and user[1] == password:   
                return True
        connection.commit()
        connection.close() 
        return False
                                
    except Exception as e:
        logging.exception(e)

def decrypt_pwd(name):
    '''
    decrypts the password with the given key in database
    :param name: name of the user
    :type name: string
    :rtype: string
    '''
    connection = psycopg2.connect(
    host = '127.0.0.1',
    database = 'database',
    user = 'postgres',
    password = 'rahul11',
    port = '5432'
    )
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM user_info ''')
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == name:
                pwd = row[1]
                key = row[2]
        connection.commit()
        connection.close()
        pwd = decrypt(pwd ,key)
        return pwd
    except Exception:
        logging.exception(" check your password !")
        
def total_mem():
    '''
    returns the totl members in the group
    :param name: name of the user
    :type name: string
    :rtype: int
    '''
    connection = psycopg2.connect(
    host = '127.0.0.1',
    database = 'database',
    user = 'postgres',
    password = 'rahul11',
    port = '5432'
    )
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT name FROM user_info ''')
        rows = cursor.fetchall()
        return len(rows)
    except Exception:
        logging.exception(" ")    
        
        
def insert_user(name, pwd ):
    '''
    inserts the user and password into datbase
    
    :param name: name of the user
    :type name: string
    :param pwd: password of the user
    :type pwd: string
    :rtype: bool
    '''
    connection = psycopg2.connect(
    host = '127.0.0.1',
    database = 'database',
    user = 'postgres',
    password = 'rahul11',
    port = '5432'
    )
    cursor = connection.cursor()
    cursor.execute(
        '''INSERT INTO user_info(name,password)
            VALUES(%(name)s, %(password)s);
        ''',
        {'name': name, 'password': pwd})

    connection.commit()
    connection.close()
  
def insert_msg(name1 , name2 ,msg ,key ):
    '''
    inserts the message into db if receiver is offline    
    :param name1: name of the sender
    :type name1: string
    :param name2: name of the receiver
    :type name2: string
    :param msg:  message
    :type msg: string
    :param key: key
    :type key: string
    :rtype: bool
    '''
    connection = psycopg2.connect(
    host = '127.0.0.1',
    database = 'database',
    user = 'postgres',
    password = 'rahul11',
    port = '5432'
    )
    if (name2) == False:
        cursor = connection.cursor()
        cursor.execute(
            '''INSERT INTO messages(sender ,receiver, msg, key)
            VALUES(%(sender)s, %(receiver)s ,%(msg)s, %(key)s );
            ''',
            {'sender': name1, 'receiver': name2, 'msg' :msg , 'key':key}
        )
        connection.commit()
        connection.close()
    else:
        print(name2 + " is online")