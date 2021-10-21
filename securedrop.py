from utl import user_list
from login import login
from user_reg import user_registration
import os.path


def main():
    print("\nWould you like to: \n\n 1.) Register new user. \n 2.) Login existing user. \n 3.) Exit. \n\n")
    value = input("Enter answer (1, 2, 3): ")

    while value != "1" and value != "2" and value != "3":
        print("Incorrect entry.")
        value = input("Enter answer (1, 2, 3): ")

    if value == "1":
        print("User Registration Selected. \n")
        f = open(user_list, "a")
        user_registration(f)

    elif value == "2":
        if os.path.isfile(user_list) and os.path.getsize(user_list) > 0:
            login()
        else:
            print("\nThere are no registered users at this time. Would you like to register a new user? (yes / no) \n \n")
            answer = ""
            while answer != "yes" and answer != "no":
                answer = input("Entry: ")
            if answer == "yes":
                f = open(user_list, "w")
                user_registration(f)
            elif answer == "no":
                print("Exiting... \n")
                exit()
    elif value == "3":
        print("Exiting... \n")
        exit()


if __name__ == "__main__":
    main()
