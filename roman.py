
#letters in roman numbers
roman_letters = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};

#roman values and decimal corresponding
roman_map = {"I": 1,
        	"V": 5,
        	"X": 10,
        	"L": 50,
        	"C": 100,
        	"D": 500,
        	"M": 1000 }

#decimal big orders
nb_orders = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

#decimal big orders and roman corresponding
orders_roman_map = {1000: "M",
					900: "CM", 
					500: "D",
					400: "CD",
					100: "C",
					90: "XC",
					50: "L",
					40: "XL",
					10: "X",
					9: "IX",
					5: "V",
					4: "IV",
					1: "I"}

def validate(entry):

	unvalid_msg = "Not a Roman Number: "
	size = len(entry)
	i = 0
	for nn in entry : #iterate over the given string
		
		in_pattern = False
		for mm in roman_letters :
			if nn == mm :
				in_pattern = True 

		if not in_pattern : #if has any letters not in the roman pattern, return false, invalid input
			print(unvalid_msg + "Entered number contains character(s) not in the roman number pattern")
			return False
		else :
			#Check for more the 3 repeated I's
			no_more_than_three = {'I', 'X', 'C'}
			for mm in no_more_than_three :
				if i+3 < size and entry[i] == mm and entry[i+1] == mm and entry[i+2] == mm and entry[i+3] == mm :
					print(unvalid_msg + "Entered number has more than 3 repeated '" + mm)
					return False

			no_more_than_one = {'V', 'L', 'D'}
			for mm in no_more_than_one :
				if i+1 < size and entry[i] == mm and entry[i+1] == mm :
					print(unvalid_msg + "Entered number has more than 1 '" + mm)
					return False

		i = i + 1;

	return True

def roman_to_int(roman_nb):
	
	value = 0
	nextValue = 0
	i = len(roman_nb)-1 #reads from right to left
	
	while i >= 0 :

		nn = roman_nb[i]
		val = roman_map[nn]

		if val >= nextValue :
			value += val
			nextValue = val
		else :
			value -= val

		i = i-1

	#print(str(roman_nb)+": "+str(value))

	return value

def int_to_roman(decimal_nb):

	roman_nb = ''
	i = 0
	while decimal_nb > 0 :
		if (decimal_nb - nb_orders[i]) >= 0 :
			decimal_nb = decimal_nb - nb_orders[i] #subtract if possible to do so
			roman_nb = roman_nb + str(orders_roman_map[nb_orders[i]]) #concat subtracted order number to form roman number
		else :
			i = i + 1

	return roman_nb

#receives two roman numbers, converts them to decimals, sum them, and gives the roman equivalent
def sum_romans(roman_one, roman_two):

	first = roman_to_int(roman_one)
	second = roman_to_int(roman_two)

	sum = first + second

	result_sum = int_to_roman(sum)

	print("Given " + 
    	str(roman_one) + " (" + str(first) + ")" + " and " +
    	str(roman_two) + " (" + str(second) + ")" + ", the result of this sum is: " + 
    	str(sum) + " (" + str(result_sum) + ")" )

	return result_sum
