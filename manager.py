# A simple password manager that allows for safe storage and retrieval of passwords

import json
import helper

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
    helper.login(username)