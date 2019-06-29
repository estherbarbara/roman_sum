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

    #Sum
    result_sum = sum_romans(entry_one, entry_two)