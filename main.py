from roman import *

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

    first = roman_to_int(entry_one)
    second = roman_to_int(entry_two)

    sum = first + second
    result_sum = int_to_roman(sum)

    print("Given " + 
    	str(entry_one) + " (" + str(first) + ")" + " and " +
    	str(entry_two) + " (" + str(second) + ")" + ", the result of this sum is: " + 
    	str(sum) + " (" + str(result_sum) + ")" )
