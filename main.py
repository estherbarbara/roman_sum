from roman import romanToInt

def validate(self):
	return 0

if __name__ == '__main__':
    #Reading numbers
    entry_one = input("Enter first roman number: ")
    entry_two = input("Enter second roman number: ")
    
    first = romanToInt(entry_one)
    second = romanToInt(entry_two)

    print("Given " + str(entry_one) + " and " + str(entry_two) + ", the result of this sum is: " + str(first + second) )
