import unittest
import MCD

class TestEjemplo(unittest.TestCase):

    def setUp(self):
        pass

    def test_maximum_community_divisor(self):
        self.assertEqual(MCD.mcd('12','6'),'6')

    def test_fails_integers_and_strings(self):
        self.assertRaises(TypeError, lambda: MCD.mcd("2","j"))

    def test_fails_with_both_strings(self):
        self.assertRaises(Exception, lambda: MCD.mcd("i","j"))

    def test_fails_with_one_integer(self):
        self.assertRaises(Exception, lambda: MCD.mcd("i"))

if __name__ =='__main__':
    unittest.main()