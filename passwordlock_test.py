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
    
    def test_init (self):
        """
        A test case for checking the validity of properties initialization
        """
        