from utl import user_list, max_times, email
from utl import check_email, get_password, hash_password
import utl
import json


def login_check():

    login_attempts = 0
    isPasswordCorrect = False
    global email
    email_data = check_email()
    utl.email = email

    json_data = open(user_list)
    data_j = json.load(json_data)
    user_data = data_j["Users"]

    if email_data in user_data[0]:
        print("Email Verified.")
        while login_attempts < max_times:
            password = get_password()
            old_password = ""
            salt = ""

            with open(user_list) as f:
                info = json.load(f)
                for p in info["Users"]:
                    salt = p[email_data]["salt"]
                    old_password = p[email_data]["password"]

            new_password = hash_password(password, salt)
            if old_password == new_password:
                print("Password Verified.")
                isPasswordCorrect = True
                exit()
            else:
                login_attempts = login_attempts + 1
                print("Password Incorrect. Please try again. You have ",
                      max_times - login_attempts, " attempts remaining.")
                isPasswordCorrect = False

    else:
        print("Email not registered. Exiting now.")

    return isPasswordCorrect


def login():
    login_check()
