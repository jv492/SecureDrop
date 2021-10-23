from utl import add_contact, user_list
import login
from user_reg import user_registration
import os.path

#function for displaying the main login menu
def main():
    print("\nWould you like to: \n\n 1.) Register new user. \n 2.) Login existing user. \n 3.) Exit. \n\n")
    value = input("Enter answer (1, 2, 3): ")

    #verifying input
    while value != "1" and value != "2" and value != "3":
        print("Incorrect entry.")
        value = input("Enter answer (1, 2, 3): ")

    #User Registration
    if value == "1":
        print("User Registration Selected. \n")
        file = open(user_list, "w")
        user_registration(file)

    #User Login
    elif value == "2":
        #if there are no users registered
        if os.path.isfile(user_list) and os.path.getsize(user_list) > 0:
            login.login()
        #if there are registered users already
        else:
            print("\nThere are no registered users at this time. Would you like to register a new user? (yes / no) \n \n")
            answer = ""
            while answer != "yes" and answer != "no":
                answer = input("Entry: ")
            if answer == "yes":
                file = open(user_list, "w")
                user_registration(file)
            elif answer == "no":
                print("Exiting... \n")
                exit()

    #User Exit
    elif value == "3":
        print("Exiting... \n")
        exit()


#Function to display user options when logged in.
def welcome():
    print("Welcome to SecureDrop.\nType \"help\" to view a list of available commands.\n")
    inp = input("Input: ")
    menu(inp)

#Function to verify user input of available options
def menu(inp):
    #display help
    if inp.lower() == "help":
        print('''
        \"Add\"  -> Add a new contact.\n\
        \"List\" -> List all online contacts.\n\
        \"Send\" -> Tansfer a file to a contact.\n\
        \"Exit\" -> Exit SecureDrop.\n
        ''')

        inp = input("Input: ")
        menu(inp)
    #add contact
    elif inp.lower() == "add":
        add_contact()
        menu("help")
    #list contacts (not yet implemented.)
    elif inp.lower() == "list":
        print("Function not yet implemented.\nExiting now...\n")
        exit()
    #send file (not yet implemented)
    elif inp.lower() == "send":
        print("Function not yet implemented.\nExiting now...\n")
        exit()
    #exit
    elif inp.lower() == "exit":
        print("Exiting now...\n")
        exit()
    #if input is invalid
    else:
        print("Input not recognized. Please try again.")
        menu("help")

if __name__ == "__main__":
    main()
