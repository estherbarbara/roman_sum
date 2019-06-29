import unittest

from roman import *

sums = {
	'VI': ['V','I'],
	'X': ['V','V'],
	'II': ['I','I'],
	'III': ['I','II'],
	'III': ['II','I'],
	'IV': ['II','II'],
	'V': ['II','III'],
	'V': ['I','IV'],
	'XL': ['XX','XX'],
	'L': ['XX','XXX'],
}

int_to_roman_tests = { 1:"I", 2: "II", 3: "III", 4: "IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
				10: "X", 11:"XI", 12:"XII", 13:"XIII", 14:"XIV", 15:"XV",
	        	50: "L", 55: "LV", 57: "LVII", 60: "LX", 70: "LXX", 80: "LXXX",
	        	100: "C",
	        	500: "D",
	        	544: "DXLIV",
	        	545: "DXLV", 639:"DCXXXIX", 646:"DCXLVI", 657:"DCLVII",
	        	1000: "M", 2000: "MM", 2400:"MMCD", 3500:"MMMD", 4000:"MMMM"}

not_roman_tests = { "XXXX", "XIIII", "CCCC", "LLLL",
	        		"LL", "VV", "DD", "MDD", "aa", "s", "KA"}

class TestSum(unittest.TestCase):

    def test_translation_roman_to_int(self):
    	for i in int_to_roman_tests.keys():
	        data = int_to_roman_tests[i]
	        result = roman_to_int(data)
	        self.assertEqual(result, i)

    def test_valid_roman_number(self):
    	for i in int_to_roman_tests.keys():
	        data = int_to_roman_tests[i]
	        result = validate(data)
	        self.assertTrue(result)

    def test_invalid_roman_number(self):
    	for i in not_roman_tests:
	        result = validate(i)
	        self.assertFalse(result)

    def test_translation_int_to_roman(self):
    	int_tests = dict(map(reversed, int_to_roman_tests.items()))
    	for i in int_tests.keys():
	        data = int_tests[i]
	        result = int_to_roman(data)
	        self.assertEqual(result, i)

    def test_sum(self):
    	for i in sums.keys():
	        data = sums[i]
	        result_sum = sum_romans(data[0], data[1])
	        self.assertEqual(result_sum, i)

if __name__ == '__main__':
    unittest.main()