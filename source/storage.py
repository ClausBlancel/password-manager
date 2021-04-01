import os
import hashlib

PATH = '/Users/vincent/Desktop/password.txt'

def create_file () : 
    file = open(PATH, "w")

def hash_password (password : str) -> str :
    return hashlib.md5(password.encode()).hexdigest()
print(hash_password('test'))

