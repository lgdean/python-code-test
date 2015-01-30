import unittest
from program import *

class TestVariousThings(unittest.TestCase):
    def test_parse_gender(self):
        self.assertEqual("Androgynous", parse_gender("Androgynous"))
        self.assertEqual("Bigender", parse_gender("bigender")) # might as well

    def test_parse_gender_special_cases(self):
        self.assertEqual("Female", parse_gender("F"))
        self.assertEqual("Female", parse_gender("f"))
        self.assertEqual("Female", parse_gender("Female"))
        self.assertEqual("Fluid", parse_gender("Fluid")) # normal case
        self.assertEqual("Male", parse_gender("M"))
        self.assertEqual("Male", parse_gender("Male"))
        return

if __name__ == '__main__':
    unittest.main()
