import string
import random

class User:
    """
    A user class that creates all user instances.
    """
    
    userList = []
    
    def __init__(self, username, password):
        """
        A method that defines the username and password properties of users
        """
        
        self.username = username
        self.password = password
    
    def  store_user(self):
        """
        A method to store user instances into the userList
        """
        User.userList.append(self)
        
        
    @classmethod
    def show_user(cls):
        return cls.userList
    
        
        
        
        
        
        