from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
#given a string this function should return  list of encrpted string and key

def encrypt(stringTE):
    '''encrypts the string with a random generated key
    : param stringTE: string to be encrypted
    : type stringTE: string 
    '''
    # if the user is offline then use this function to encrypt the messages
    # or use this for storing passwords 
    hkdf = HKDF(
        algorithm=hashes.SHA256(),  
        length=32,
        salt=None,    
        info=None,    
        backend=default_backend()
        )
    
    key = base64.urlsafe_b64encode(hkdf.derive(b"stringTE"))
    f = Fernet(key)
    Estring = f.encrypt(stringTE.encode()) # encrypted string
    return [Estring,key]

def decrypt(Estring,key):
    '''decrypts the string with the key in database
    : param EtringTE: string to be encrypted
    : type  EtringTE: string 
    '''
    # if the user is online then check if the user have any messages to be delivered and the decrypt
    # all the messages and send to the client if client want to see the messages 
    hkdf = HKDF(
        algorithm=hashes.SHA256(),  
        length=32,
        salt=None,    
        info=None,    
        backend=default_backend()
    )
    keyToDecrypt=Fernet(key)
    dSrting=keyToDecrypt.decrypt(Estring).decode()
    return dSrting


    
    
