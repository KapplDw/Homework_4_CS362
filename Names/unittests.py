import unittest
import fullname

class LearnTest(unittest.TestCase):

    def test_name(self):

        self.assertEqual(fullname.fullName("Dwight", "Kappl"), "Dwight Kappl")
        
        self.assertEqual(fullname.fullName("", "Empty"), " Empty")
        # Fail case
        self.assertEqual(fullname.fullName("Failure", 123), -1) # Fail Case

    

        

if __name__ == "__main__":
    unittest.main()
