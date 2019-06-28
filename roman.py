
roman_map = {"I": 1,
        	"V": 5,
        	"X": 10,
        	"L": 50,
        	"C": 100,
        	"D": 500,
        	"M": 1000 }

def validate(entry):
	
	#letters in roman numbers
	roman_letters = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};

	size = len(entry)
	i = 0
	for nn in entry : #iterate over the given string
		
		in_pattern = False
		for mm in roman_letters :
			if nn == mm :
				in_pattern = True 

		if not in_pattern : #if has any letters not in the roman pattern, return false, invalid input
			print("Entered number not a Roman Number\n")
			return False
		else :
			#Check for more the 3 repeated I's
			noMoreThanThree = {'I', 'X', 'C'}
			for mm in noMoreThanThree :
				if i+3 < size and entry[i] == mm and entry[i+1] == mm and entry[i+2] == mm and entry[i+3] == mm :
					print("Entered number has more than 3 repeated '" + mm + "' \n")
					return False

			noMoreThanOne = {'V', 'L', 'D'}
			for mm in noMoreThanOne :
				if i+1 < size and entry[i] == mm and entry[i+1] == mm :
					print("Entered number has more than 1 '" + mm + "' \n")
					return False

		i = i + 1;

	return True

def roman_to_int( roman_nb ):
	
	value = 0
	nextValue = 0
	i = len(roman_nb)-1
	
	while i >= 0 :

		nn = roman_nb[i]
		val = roman_map[nn]

		if val >= nextValue :
			value += val
			nextValue = val
		else :
			value -= val

		i = i-1

	#print(str(roman_nb)+"-"+str(value))

	return value

def int_to_roman( roman_nb ):

	int_tests = dict(map(reversed, roman_map.items()))
	
	return "not yet implemented"