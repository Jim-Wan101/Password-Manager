# A simple password manager that allows for safe storage and retrieval of passwords

import os
import json

welcome_message = """
=========================
Welcome to Password Manager!
Please L to login or R to register
=========================
"""

def register(username):
    pass


def login_choice():
    login_choice = input()

    if login_choice == "L":
        username = input("Username: ")
        return "login", username
    elif login_choice == "R":
        username = input("Please input your desired username: ")
        return "register", username
    else:
        print("Please enter a valid command")
        login_choice()

def login(username):
    pass

print(welcome_message)

action, username = login_choice()

if action == "register":
    register(username)
else:
    login(username)