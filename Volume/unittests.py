import unittest
import volume

class LearnTest(unittest.TestCase):

    def test_volume(self):
        
        self.assertEqual(volume.volume(5, 5, 5), 125)
        self.assertEqual(volume.volume(2**2, 20, 10), 800)
        # Fail case
        self.assertEqual(volume.volume(1,-2, 1), 2) # Fail Case
    

        

if __name__ == "__main__":
    unittest.main()
