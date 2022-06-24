import unittest
from roman_numerals import roman_numeral

class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(roman_numeral(1).tostring(), 'I')  # add assertion here

    def test_two(self):
        self.assertEqual(roman_numeral(2).tostring(), 'II')  # add assertion here

    def test_three(self):
        self.assertEqual(roman_numeral(3).tostring(), 'III')  # add assertion here

    def test_four(self):
        self.assertEqual(roman_numeral(4).tostring(), 'IV')  # add assertion here

    def test_five(self):
        self.assertEqual(roman_numeral(5).tostring(), 'V')  # add assertion here

    def test_six(self):
        self.assertEqual(roman_numeral(6).tostring(), 'VI')  # add assertion here

    def test_seven(self):
        self.assertEqual(roman_numeral(7).tostring(), 'VII')  # add assertion here

    def test_nine(self):
        self.assertEqual(roman_numeral(9).tostring(), 'IX')  # add assertion here

    def test_ten(self):
        self.assertEqual(roman_numeral(10).tostring(), 'X')  # add assertion here

    def test_nineteen(self):
        self.assertEqual(roman_numeral(19).tostring(), 'XIX')  # add assertion here

    def test_twentyfour(self):
        self.assertEqual(roman_numeral(24).tostring(), 'XXIV')  # add assertion here

    def test_fourtynine(self):
        self.assertEqual(roman_numeral(49).tostring(), 'XLIX')  # add assertion here

    def test_eightyone(self):
        self.assertEqual(roman_numeral(81).tostring(), 'LXXXI')  # add assertion here

    def test_onethousendninetynine(self):
        self.assertEqual(roman_numeral(1099).tostring(), 'MXCIX')  # add assertion here
    def test_twothousandtwohundredfiftyfour(self):
        self.assertEqual(roman_numeral(2254).tostring(), 'MMCCLIV')  # add assertion here

if __name__ == '__main__':
    unittest.main()
