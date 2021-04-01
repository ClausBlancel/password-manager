import os
import hashlib

"""
TODO : 
    add a PATH 
    transfer the password string from the password generator
"""

password = 'HelloWorld'

def store_in_file (password : str) : 
    file = open('password.txt', "w")
    file.write(hash_password(password))
    file.close()


def hash_password (password : str) -> str :
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == "__main__" : 
    store_in_file(password)

# print(hash_password('test'))

