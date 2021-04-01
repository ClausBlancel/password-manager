import re

def password_length (password : str) -> bool :
    return (len(password)>8)

def uppercase (password : str) -> bool : 
 
    if (re.search(r"[A-Z]", password) ) :
        return True
    else : 
        return False

def lowercase (password : str) -> bool : 
    if (re.search(r"[a-z]", password)) : 
        return True
    else : 
        return False

def special_char (password : str) -> bool : 
    if (re.search (r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password)) : 
        return True 
    else : 
        return False

def password_strength (password : str) -> bool : 
    if ((password_length(password)) and (uppercase(password)) and (lowercase(password)) and (special_char(password))) : 
        return True 
    else : 
        return False

print(password_strength("aaAAiAAA#A"))
