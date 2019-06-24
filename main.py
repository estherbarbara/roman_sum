from roman import romanToInt
from roman import validate

if __name__ == '__main__':
    
    #Reading numbers
    valid = False
    while not valid:
    	entry_one = input("Enter first roman number: ")
    	if validate(entry_one):
    		valid = True

    valid = False
    while not valid:
    	entry_two = input("Enter second roman number: ")
    	if validate(entry_two):
    		valid = True

    first = romanToInt(entry_one)
    second = romanToInt(entry_two)

    print("Given " + str(entry_one) + " and " + str(entry_two) + ", the result of this sum is: " + str(first + second) )
