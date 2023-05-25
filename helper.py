import os
import json
import base64
from cryptography.fernet import Fernet 

def register(username):
    with open("data.json", "r") as file:
        content = json.load(file)

    for i in range(len(content["accounts"])):
        if username == content["accounts"][i]["username"]:
            print("Username is already taken!")
            username = input("Please choose another username: ")
            register(username)
    
    content["accounts"].append({
        "username": username,
    })

    with open("data.json", "w") as file:
        json.dump(content, file, indent=4)


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
    with open("data.json", "r") as file:
        content = json.load(file)

    for i in range(len(content["accounts"])):
        if username == content["accounts"][i]["username"]:
            password = input("Please enter your password: ")

            if password == content["accounts"][i]["password"]:
                return "success", i
            else:
                print("The password entered is incorrect")
                return "fail", i

def print_options():
    print("=========================")
    print("Enter L to see a list of acount names for your passwords")
    print("Enter V, followed by an account name, to view the password saved for the account")
    print("Enter S to store a new password")
    print("Enter C to change a saved password")
    print("Enter D to delete your account")
    print("Enter X to logout")
    print("=========================")
    
    action = input()

    return action

def print_list(username, i):
    with open("data.json", "r") as file:
        content = json.load(file)
    
    for entry in content["accounts"][i]["store"]:
        print(*entry)

def delete_account(username):
    with open("data.json", "r") as file:
        content = json.load(file)
    
    for i in range(len(content["accounts"])):
        if username == content["accounts"][i]["username"]:
            del content["accounts"][i]
            break

    with open("data.json", "w") as file:
        json.dump(content, file, indent=4)
            
def view_password(name, i):
    with open("data.json", "r") as file:
        content = json.load(file)
    
    for obj in content["accounts"][i]["store"]:
        for key, value in obj.items():
            if key == name:
                print(value)
                break

    print("Username not found. Enter V to try again")

def store_password(account_name, i):
    with open("data.json", "r") as file:
        content = json.load(file)

    key = input("Please enter a 8 character secret key: ").encode()
    key = key.ljust(32, b"=")
    key = base64.urlsafe_b64encode(key)
    key = Fernet(key)

    password = input("Please input the password you would like to encrypt: ")

    encrypted_password = key.encrypt(password.encode())

    content["accounts"][i]["store"].append({
        account_name: encrypted_password.decode()
    })

    with open("data.json", "w") as file:
        json.dump(content, file, indent=4)