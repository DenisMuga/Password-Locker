# PASSWORD LOCKER

## Author

[DenisMuga](https://github.com/DenisMuga)

## Description

Password Locker is a python application that acts a manager for login and signup credentials of individuals with for several accounts. The credentials are usernames and passwords for different accounts. The application also keeps passwords and generates password at users'requests.

## User Stories
The user would like to.... :
* To log into the application or create a new account.
* Store existing acounts and login credentials for the same.
* Generate random password for unregistered accounts and store it using an account name.   
* Delete the unwanted but existing account login credentials.

## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.8.10
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/DenisMuga/Password-Locker.git```

* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ ./view.py

* To run test for the application
        $ python3 passwordlock_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command $ ./view.py |Welcome To Personal Accounts Locker. \n To proceed, Enter: \n CA=Create Account \n LG=Have Account \n
|Type  CA| input username and password| Hello 'username, You successfully created an Account: Your Password is: ```password```|
|Type LG  | Enter your password and username you provide during sign up| Acronyms like TP are provided to help navigate the application|
|Introduce a new credential| Enter CC|Enter Account, username, password, choose ```tp``` to type your password or ```gp``` to generate a new password from the application|
|Show existing credentials | Type DC |Prompts a list of stored credentials or The Credential Does Not Exist For Deletion |
|Use account name to find a stored credential|Type FC | Enter the Account Name for search fto show the account details|
|Purge unwanted credential|Type D|Type the account name of a particular credential. Returns TRUE if account is deleted and FALSE if the account doesn't exist|
|Exit the application| Type EX| The application exits|

## Technologies Used

* python3.8.10

## Known Bugs
* Application works perfectly. Contact me through the contacts in case any is found.

## Contact Information 

For questions, comments, and contributions, contact me through [denismugah5@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Denis Muga**
