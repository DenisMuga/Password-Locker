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
    
    