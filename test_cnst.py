import unittest
from cnst import cnst

class TestBuiltins(unittest.TestCase):
    def test_cnst(self):
        for i in range(-1000, 1001): 
            self.assertEqual(cnst(i), i)

if __name__ == '__main__':
    unittest.main()
