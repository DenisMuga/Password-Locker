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
        
        