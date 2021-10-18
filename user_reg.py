from utl import reg_email, get_password, password_chk
from utl import hash_pw
from getpass import getpass
import json
import secrets

# Checks password and if it passes hopefully hashes it and stores

def user_registration(file):
    name = input("Enter Full Name: ")
    email = reg_email()
    password = password_chk
    second_pass = getpass("Please re-enter password: ")
    check = password_chk(password)

    # Loop until password is right
    while not check.get("password_ok") or password != second_pass:
        if password != second_pass:
            print("Wrong password.")
        elif not check.get("password_ok"):
            print(
                "Password is not strong enough. A password is strong if it has:"
                "\n 8 characters length or more"
                "\n 1 digit or more"
                "\n 1 symbol or more"
                "\n 1 uppercase or more"
                "\n 1 lowercase or more"
            )
        password = getpass("Enter password:")
        second_pass = getpass("Please re-enter password")
        check = password_chk(password)

    salt = secrets.token_hex(8)
    h_password = hash_pw(password, salt)

    dict = {}
    dict["User"] = []
    dict["User"].append({email: {"name": name, "password": h_password, "salt": salt}})
    json.dump(dict, file)
    file.close()
    print("User sucessfully registered, please login again to begin!")
    exit()