import unittest

from roman import romanToInt


roman_tests = {1:"I", 2: "II", 3: "III", 4: "IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
				10: "X", 11:"XI", 12:"XII", 13:"XIII", 14:"XIV", 15:"XV",
	        	50: "L",
	        	100: "C",
	        	500: "D",
	        	544: "DXLIV",
	        	545: "DXLV", 639:"DCXXXIX", 646:"DCXLVI", 657:"DCLVII",
	        	1000: "M", 2000: "MM", 2400:"MMCD", 3500:"MMMD"}

class TestSum(unittest.TestCase):
    def test_list_int(self):
    	for i in roman_tests.keys():
	        data = roman_tests[i]
	        result = romanToInt(data)
	        self.assertEqual(result, i)

if __name__ == '__main__':
    unittest.main()
    """applicant = input("Enter the applicant's name: ")"""