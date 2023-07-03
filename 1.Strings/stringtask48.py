"""Write a Python program to swap commas and dots in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"""
#input variable
string = input('Enter your text: ')
#second variable with a matching function
new_string = string.maketrans
string = string.translate(new_string(',.', '.,'))
#output
print(string)