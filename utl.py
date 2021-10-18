import re
from getpass import getpass
import crypt
import json


max_times = 3

user_list = "./user_list.json"

online_contacts = []

email = ""

user_name = ""

def password_chk(password):
    # Make sure the password is strong
    # check for  8 char length or more
    # 1 digit or more
    # 1 symbol or more 
    # 1 Uppercase and 1 lowercase letter or more

    #length
    length_err = len(password) < 8

    #look for digits
    digit_err = re.search(r"\d", password) is None

    #Search for uppercase
    upcase_err = re.search(r"[A-Z]", password) is None

    #Search for lowercase
    lowcase_err = re.search(r"[a-z]", password) is None

    #search for symbols
    symbol_err = re.search(r"\W", password) is None

    password_ok = not (
        length_err
        or digit_err
        or upcase_err
        or lowcase_err
        or symbol_err

    )

    return{
        "password_ok": password_ok,
        "length_error": length_err,
        "digit_error": digit_err,
        "uppercase_error" : upcase_err,
        "lowercase_error" : lowcase_err,
        "symbol_error": symbol_err,
    }

def get_password():
    password = getpass("Enter password: ")
    return password

def reg_email():
    email = input("Enter E-mail:")
    return email

def get_email_and_password():
    password = get_password()
    email = reg_email()
    return(email, password)

def check_email():
    # Makes user to enter there password
    # User has 3 tries

    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    attemps = 0

    while attemps < max_times:
        email = input("Enter E-mail: ")
        if re.search(regex, email):
            print("vaild E-mail")
            attemps = max_times
            return email
        else:
            print("Invaild E-mail")
            attemps += 1
    return None

def hash_pw(password, salt):
    return crypt.crypt(password, salt)

# Make sure Email does not already exits these next three function will check that

def user_contact_exist(user_dict, email):
    count = 0
    for x in user_dict:
        if user_dict[count].get("email") == email:
            return True
        count += 1
    return False


