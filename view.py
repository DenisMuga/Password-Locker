#!/usr/bin/env python3.8
from passwdlock import User, Credentials

def function():
    print("PASSWORD LOCKER")
function()

def create_new_user(username, password):
    """
    A function to create a new user with username and passowrd properties
    """
    new_user = User(username, password)
    return new_user
    
def store_user(user):
    """
    A function to store a new user
    """
    User.store_user()
    
def show_user():
    """
    A function that shows an existing user
    """
    return User.show_user()

def login_user(username, password):
    """
    A function to check if  users exist and logs them in
    """
    find_user = Credentials.check_user(username, password)
    return find_user
def create_new_credential(account_details,user_name, password):
    """
    A function to create new credentials for each user account
    """
    new_credential = Credentials(account_details,user_name, password)
    return new_credential

def store_credentials(credentials):
    """
    A function to store credentials to the credentialList
    """
    credentials.store_credentials()
def delete_credentials(credentials):
    """
    A function to delete credentials form credentialList
    """
    credentials.delete_credentials()
    
def show_acc_details():
    """
    A function to display all saved credentials
    """
    return Credentials.show_credentials()
    