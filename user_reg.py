from utl import reg_email, get_password, password_chk
from utl import hash_password, user_list
from getpass import getpass
import json
import secrets


#function to register new user
def user_registration(file):
    name = input("Enter Full Name: ")
    email = reg_email()
    password = get_password()
    second_pass = getpass("Please re-enter password: ")
    check = password_chk(password)

    #Verifying that the user is using a strong password
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
        second_pass = getpass("Please re-enter password")
        check = password_chk(password)

    #password hashing
    salt = secrets.token_hex(8)
    password = hash_password(password, salt)

    #creating an input to add to json file for user registration
    dict = {}
    dict["Users"] = []
    dict["Users"].append(
            {email: {"name": name, "password": password, "salt": salt}})
    json.dump(dict, file)
    file.close()

    print("\nUser sucessfully registered, please login again to begin!")
    exit()
