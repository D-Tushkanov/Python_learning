"""Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters. """
#input variable
string = input("Enter your text:")
#number variable
number = 0
#check for uppercase letters in the first four characters
for letter in string[:4]:
	#capitalize the rest of the characters
	if letter.upper() == letter:
		number += 1
if number >= 2:
	#output with changes
	print(string.upper())
#no change in output
print(string)