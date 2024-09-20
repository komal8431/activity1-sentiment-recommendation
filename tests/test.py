import unittest
import sys
import os

# Adjusting the system path to import the main function
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../features')))
from main import main  # Importing the main function

class TestCases(unittest.TestCase):
    def test_cases(self,choice=5):
        #calling the fn
        user_input,choice=main()
        #basic checks
        self.assertIsInstance(user_input,str,"User Input")
        self.assertIsInstance(choice,int,"Recommendation Choice")

if __name__=='__main__':
    unittest.main()