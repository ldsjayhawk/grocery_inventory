from dotenv import load_dotenv
import os
import requests
from getpass import getpass

load_dotenv()
api_key = os.getenv("FIREBASE_API_KEY")

def check_login():
    login_path = input('Would you like to login(l) or register for an account(r)? ')
    if login_path == 'l':
        return login()
    elif login_path == 'r':
        return register()
    else:
        print('Invalid Reponse')
        return check_login()


def login():
    print()
    print('Please Log in')
    email = input("Enter your email address: ")
    password = getpass("Enter your password: ")

    # create json for request
    login_info = {
        "email": email,
        "password": password,
        "returnSecureToken": True
        }

    login_user = requests.post(
        f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}',
        json=login_info)

    login_data = login_user.json()

    # check for errors
    if 'error' in login_data:
        print(login_data["error"]["message"])
        print('Please try again')
        return login()
    # elif login_data["displayName"] == None:
    #     print(f'Hello there!')
    else:
        print(f'Hello there!')

    return login_data["localId"]

def logout():
    print("logout")

def register():
    # variables for user input
    print()
    print('Register an account')
    email = input("Enter your email address: ")
    password = getpass("Enter a password: ")

    # create json for request
    reg_info = {
        "email": email,
        "password": password,
        "returnSecureToken": True
        }

    # send request with api key and json
    register_user = requests.post(
        f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}',
        json=reg_info)
    register_data = register_user.json()

    # check for errors
    if 'error' in register_data:    
        if register_data["error"]["message"] == 'EMAIL_EXISTS':
            print('Email already exists, please sign-in')
            return login()

        elif register_data["error"]["message"] != 'EMAIL_EXISTS':
            print(register_data["error"]["message"])
            return register()
    else:
        print('Registration succeeded.')

    # send user to login when complete
    return login()

# check_login()

