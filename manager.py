# A simple password manager that allows for safe storage and retrieval of passwords

import json
import helper
import sys

welcome_message = """
=========================
Welcome to Password Manager!
Enter L to login or R to register
=========================
"""

# Implement forgot password feature
# Implement security questions feature to go along with forgot password

print(welcome_message)

action, username = helper.login_choice()

if action == "register":
    helper.register(username)
else:
    status, index = helper.login(username)

while status != "success":
    username = input("Username: ")
    status = helper.login(username)

print("Login Success!")

action = helper.print_options()

while action != "X":
    if action == "L":
        helper.print_list(username, index)
    elif action == "D":
        helper.delete_account(username)
        print("Your account has been successfully deleted")
        break
    elif action == "V":
        print("Which password would you like to view?")
        account = input()
        helper.view_password(account, index)
    elif action == "S":
        print("Please enter the desired account name for your password")
        account = input()
        helper.store_password(account, index)
    action = input()

print("Exiting the program")
sys.exit()