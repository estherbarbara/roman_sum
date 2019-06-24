
def romanToInt( roman_nb ):
	
	roman_map = {"I": 1,
            	"V": 5,
            	"X": 10,
            	"L": 50,
            	"C": 100,
            	"D": 500,
            	"M": 1000 }

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

	print(str(roman_nb)+"-"+str(value))

	return value
