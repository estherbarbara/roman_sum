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
	'LX': ['XXX','XXX'],
	'LX': ['L','X'],
	'XLIX': ['XX','XXIX'],
	'DCCC': ['C','DCC'],
	'CCM': ['C','DCC'],
	'DCC': ['C','DC'],
	'MMM': ['MM','M'],
	'MMMII': ['MMI','MI'],
	'LXXIV': ['XIV','LX']
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
	        		"LL", "VV", "DD", "MDD", "aa", "s", "KA", "X I"}

class TestSum(unittest.TestCase):

	#test valid inputs
    def test_valid_roman_number(self):
    	print("\n----------------------- testing valid numbers ------------------------\n")
    	for i in int_to_roman_tests.keys():
	        data = int_to_roman_tests[i]
	        result = validate(data)
	        self.assertTrue(result)

	#test invalid inputs
    def test_invalid_roman_number(self):
    	print("\n----------------- running test: invalid numbers ----------------------\n")
    	for i in not_roman_tests:
	        result = validate(i)
	        self.assertFalse(result)

    def test_translation_roman_to_int(self):
    	print("\n--------- running test: valid translation roman to decimal -----------\n")
    	for i in int_to_roman_tests.keys():
	        data = int_to_roman_tests[i]
	        result = roman_to_int(data)
	        self.assertEqual(result, i)

	#revert the dict to translate in the oposite direction (int to roman) as previous test (roman to int)
    def test_translation_int_to_roman(self):
    	print("\n---------- running test: valid translation decimal to roman ----------\n")
    	int_tests = dict(map(reversed, int_to_roman_tests.items()))
    	for i in int_tests.keys():
	        data = int_tests[i]
	        result = int_to_roman(data)
	        self.assertEqual(result, i)

	#consider dict values converted to decimal
    def test_sum_1(self):
    	print("\n----------------- running test: sum numbers one ---------------------\n")
    	for i in sums.keys():
	        data = sums[i]
	        result_sum = sum_romans(data[0], data[1])
	        self.assertEqual(roman_to_int(result_sum), roman_to_int(i)) #reassuring that the received converted values to decimal are the same

	#consider sum of the given values converted to decimal
    def test_sum_2(self):
    	print("\n----------------- running test: sum numbers two ---------------------\n")
    	for i in sums.keys():
	        data = sums[i]
	        result_sum = sum_romans(data[0], data[1])
	        sum_x = roman_to_int(data[0]) + roman_to_int(data[1]) #translates the given romans and gives their sum in decimal
	        sum_result = roman_to_int(result_sum) #translates the resulted sum
	        self.assertEqual(sum_result, sum_x)

if __name__ == '__main__':
    unittest.main()