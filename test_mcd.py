import unittest
from mcd import MCD
import mock
import mongomock

class TestMCD(unittest.TestCase):

    def setUp(self):
        self.mcd = MCD()
        self.mcd.client = mongomock.MongoClient()
        self.mcd.db = self.mcd.client[self.mcd.DATABASE_NAME]

    def testSave(self):

        def test_maximum_community_divisor(self):
            self.assertEqual(self.mcd.calcular_mcd('12','6'),'6')

        def test_fails_integers_and_strings(self):
            self.assertRaises(TypeError, lambda: self.mcd.calcular_mcd("2","j"))

        def test_fails_with_both_strings(self):
            self.assertRaises(Exception, lambda: self.mcd.calcular_mcd("i","j"))

        def test_fails_with_one_integer(self):
            self.assertRaises(Exception, lambda: self.mcd.calcular_mcd("i", None))

    def testGetMcds(self):

        def test_fail_wrong_quantity(self):
            MCD.get_mcds = mock.MagicMock(['0','2','3'])
            assertEquals(MCD.resultado, [('1','2','3')])

if __name__ =='__main__':
    unittest.main()