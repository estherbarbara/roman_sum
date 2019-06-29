from roman import *

if __name__ == '__main__':
    
    #Reading numbers
    valid = False
    while not valid:
    	entry_one = input("Enter first roman number: ")
    	if validate(entry_one):
    		valid = True
    	else :
    		print("Entered number contains character(s) not in the roman number pattern")

    valid = False
    while not valid:
    	entry_two = input("Enter second roman number: ")
    	if validate(entry_two):
    		valid = True
    	else :
    		print("Entered number contains character(s) not in the roman number pattern")

    #Sum
    result_sum = sum_romans(entry_one, entry_two)

    print( str(entry_one) + " + " + str(entry_two) + " = " + str(result_sum) )