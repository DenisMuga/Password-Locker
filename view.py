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

def verify_credential(account_details):
    """
    A function that uses account name to find credentials and returns credentials of that particular account
    """
    return Credentials.verify_credential(account_details)

def credential_existence(account_details):
    """
    A function that checks if a credential exists with a particular account name and return True or False
    """
    return Credentials.if_credential_existence(account_details)
def generatePassword():
    """
    A function that generates users random password
    """
    rand_password = Credentials.generatePassword()
    return rand_password
    
    
def passwordlocker():
    print("Welcome To Personal Accounts Locker. \n To proceed, Enter: \n CA=Create Account \n LG=Have Account \n")
    user_choice = input("").lower().strip()
    if user_choice == "ca":
        print("Sign Up")
        print('-' * 60)
        username = input("User_name: ")
        while True:
            print("TP = Type Own Password: \n GP = Generate Random Password")
            pwdChoice = input("").lower().strip()
            if pwdChoice == 'tp':
                password = input("Enter Password\n")
                break
            elif pwdChoice == 'gp':
                password = generatePassword()
                break
            else:
                print("Wrong Password, Please Try Again")
        store_user(create_new_user(username,password))
        print("-" *100)
        print(f"Hello {username}, You successfully created an Account: Your Password is: {password}")
        print("-" * 100)
    elif user_choice == "lg":
        print("-" * 60)
        print("To Login, Enter Username and Password:")
        print("-" * 50)
        username = input("User Name: ")
        password = input("Password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}. Welcome to Password Locker Manger")
            print('\n')
    while True:
        print("Please Use These Short Codes:\n CC = Create a New Credential \n DC = Display Credentials \n FC = Find a New Credential \n GP=Generate Random Password \n DD = Delete Credential \n EX = Exit the Application \n")
        user_choice = input("").lower().strip()
        if user_choice == 'cc':
            print("Create New Credential")
            print("-" * 30)
            print("Account Name: ")
            account_details = input().lower()
            print("Input Account Username")
            user_name = input()
            while True:
                print("TP- Type Own Password If You Have Account Already: \n GP - Generate Random Password")
                pwdChoice = input().lower().strip()
                if pwdChoice == "tp":
                    password = ("Enter Your Own Password\n")
                    break
                elif pwdChoice == 'gp':
                    password = generatePassword()
                    break
                else:
                    print("Invalid Password Please: Try Again!")
            store_credentials(create_new_credential(account_details, user_name, password))
            print("\n")
            print(f"Account Credential for {account_details}, User name: {user_name}, Passwor: {password} is successfully created")
            print("\n")
        elif user_choice == "dc":
            if show_acc_details():
                print(f"Account: {account_details.account_details} \n User name: {user_name} \n Password: {password}")
                print("-" * 40)
                print("-" * 40)
            else:
                print("None of Your Credentials Saved!")
        elif user_choice == "DD":
            print("Enter Account Name for the Credentials You Want to Delete")
            search_name = input().lower()
            if verify_credential(search_name):
                get_credential = verify_credential(search_name)
                print("-" * 60)
                get_credential.delete_credentials()
                print("\n")
                
            else:
                print("The Credential Does Not Exist For Deletion")
        elif user_choice == "gp":
            password = generatePassword()
            print(f"{password} Has Been Successfully Generated! Proceed to Use It in Your Account")
        elif user_choice == "ex":
            print("Thank You For Using Password Locker!! See You Later!!")
            break
        else:
            print("Wrong Entry! Please Check Menu Entries and Match!")
            
if __name__ == '__main__':
    passwordlocker()
            
                
        

                
                

                    
            
            
        
        

            
    

