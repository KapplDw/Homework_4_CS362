import unittest
import average

class LearnTest(unittest.TestCase):

    def test_volume(self):
        
        self.assertAlmostEqual(average.average((-1, -5, -120, -5, -10)), -29)
        
        self.assertEqual(average.average((1, 2, 3, 4, 5)), 3)
        # Fail case
        self.assertEqual(average.average((a, b, c, d, e) ), -1) # Fail Case
    

        

if __name__ == "__main__":
    unittest.main()
