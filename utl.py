import re
from getpass import getpass
import crypt
import json

#global veriables
max_times = 3

user_list = "./user_list.json"

email = ""

user_name = ""

#function to ensure the password is strong
def password_chk(password):
    # Make sure the password is strong
    # check for  8 char length or more
    # 1 digit or more
    # 1 symbol or more
    # 1 Uppercase and 1 lowercase letter or more

    # length
    length_err = len(password) < 8

    # look for digits
    digit_err = re.search(r"\d", password) is None

    # Search for uppercase
    upcase_err = re.search(r"[A-Z]", password) is None

    # Search for lowercase
    lowcase_err = re.search(r"[a-z]", password) is None

    # search for symbols
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
        "uppercase_error": upcase_err,
        "lowercase_error": lowcase_err,
        "symbol_error": symbol_err,
    }

#get password using getpass
def get_password():
    password = getpass("Enter password: ")
    return password

#register email
def reg_email():
    email = input("Enter E-mail:")
    return email

#get email and password
def get_email_and_password():
    password = get_password()
    email = reg_email()
    return(email, password)

#confirming email is correct using regex
def check_email():
    # Makes user to enter their password
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

#encrypt password
def hash_password(password, salt):
    return crypt.crypt(password, salt)

#add new contact
def add_contact():
    file = open('user_list.json', 'r+')
    data = json.load(file)

    user_email = list(data["Users"][0].keys())[0]
    u_dictionary = data["Users"][0][user_email]
    name = input("Enter Full Name: ")
    email = reg_email()
    u_dictionary["contacts"] = [
        {"email": email, "name": name}
    ]
    data["Users"][0][user_email] = u_dictionary
    file.seek(0)
    json.dump(data, file)
    print("\nContact added successfully.\n")
    file.close()