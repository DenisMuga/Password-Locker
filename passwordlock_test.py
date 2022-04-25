import unittest
from passwdlock import User
from passwdlock import Credentials

class TestClass(unittest.TestCase):
    """
    A test class for various User Class test cases
    """
    def setUp(self):
        """
        A method that executes before each test case
        """
        self.new_user = User('DenisMuga','Mu20muD5')
    
    def test_init(self):
        """
        A test case for checking the validity of properties initialization
        """
        self.assertEqual(self.new_user.username, 'DenisMuga')
        self.assertEqual(self.new_user.password, 'Mu20muD5')
        
    def test_store_user(self):
        """
        A test case for checking if new user instances are saved in the userList
        """
        self.new_user.store_user()
        self.assertEqual(len(User.userList),1)
        
class TestCredentials(unittest.TestCase):
    """
    A test class for defining credentials test cases
    """
    def setUp(self):
        """
        A method that executes before each test case
        """
        self.new_credential = Credentials('Gmail', 'Denis_Muga', 'Mx20mcD7')
        
    def test_init(self):
        """
        A test case to verify if new instances of credentials are correctly initialized
        """
        self.assertEqual(self.new_credential.account_details,'Gmail')
        self.assertEqual(self.new_credential.user_name, 'Denis_Muga')
        self.assertEqual(self.new_credential.password, 'Mx20mcD7')
        
    def store_credentials_test(self):
        """
        A test case to check if objects in the credentials are saved in the credentialList
        """
        self.new_credential.store_credentials()
        self.assertEqual(len(Credentials.credentialList),1)
        
    def tearDown(self):
        """
        A test case to clean up after each test case has run.
        """
        
        Credentials.credentialList = []
        
    def test_store_many_account_details(self):
        """
        A test case to check if we can store many credentials account objects to credentialList
        """
        self.new_credential.store_credentials()
        test_credential = Credentials("Facebook", "denismuga", "Jd12klx8")
        test_credential.store_credentials()
        self.assertEqual(len(Credentials.credentialList),2)
        
    def test_delete_credentials(self):
        """
        A test case to check if we can remove credentials from credentialList
        """
        
        self.new_credential.store_credentials()
        test_credential = Credentials("Facebook", "denismuga", "Jd12klx8")
        test_credential.store_credentials()
        
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentialList),1)
        
    def test_verify_credential(self):
        """
        A test case to check if it's possible to display credentials account details using account name search
        """
        
        self.new_credential.store_credentials()
        test_credential = Credentials("Facebook", "denismuga", "Jd12klx8")
        test_credential.store_credentials()
        
        my_credential = Credentials.verify_credential("Facebook")
        
        self.assertEqual(my_credential.account_details, test_credential.account_details)
        
    def test_credential_existence(self):
        """
        A test case to check if we can return True or False booleans based on existence or non-existence of credentials
        """
        self.new_credential.store_credentials()
        my_credential = Credentials("Facebook", "denismuga", "Jd12klx8")
        my_credential.store_credentials()
        
        found_credential = Credentials.if_credential_existence("Facebook")
        self.assertTrue(found_credential)
        
        
        
        

        
        
        
        
        
        
        
        
        