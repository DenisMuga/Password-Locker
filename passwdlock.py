from collections import UserList
from os import remove
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
        """
        A method to diplay users form the userList
        """
        return cls.userList
    
    def delete_user(self):
        """
        A method to delete users' accounts from userList
        """
        User.userList.remove(self)
        
    class Credentials():
        """
        A credentials class for holding credential objects
        """
        
        credentialList = []
        @classmethod
        def check_user(cls, username, password):
            """
            A method for checking user existence in the userList
            """
            
            app_user = ''
            for user in UserList:
                if (user.username == username and user.userpassword == password):
                    app_user = user.username
            return app_user
        
        def __init__(self,user_name, password, account_details):
            """
            A method defining users credentilas properties to be saved
            """
            
        

        
    
        
        
        
        
        
        