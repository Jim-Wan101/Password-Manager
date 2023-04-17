import os
import json

def register(username):
    with open("data.json", "r") as file:
        content = json.load(file)

        index = 0

        for i in range(len(content["accounts"])):
            if username == content["accounts"][i]["username"]:
                print("Username is already taken!")
                username = input("Please choose another username: ")
                register(username)
            index += i
        
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
    pass