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

if action == "X":
    sys.exit()
elif action == "L":
    helper.print_list(username, index)
