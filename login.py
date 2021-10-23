from utl import user_list, max_times, email
from utl import check_email, get_password, hash_password
import securedrop
import utl
import json

#login functionality
def login_check():

    #making sure the user does not have infinite login attempts
    login_attempts = 0
    global email
    email_data = check_email()
    utl.email = email

    json_data = open(user_list)
    data_j = json.load(json_data)
    user_data = data_j["Users"]

    #confirming email is registered
    if email_data in user_data[0]:
        print("\nEmail Verified.\n")
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
            #confirming password matches
            if old_password == new_password:
                print("\nPassword Verified.\n")
                securedrop.welcome()
            else:
                login_attempts = login_attempts + 1
                print("\nPassword Incorrect. Please try again. You have ",
                      max_times - login_attempts, " attempts remaining.\n")

        #if user enters too many incorrect passwords, exit.
        print("Max number of attempts reached. System is now exiting...")
        exit()

    #if email is not registered. Exit.
    else:
        print("\nEmail not registered. Exiting now.")

    return

#login
def login():
    login_check()
