"""Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""
#first variable
#string = input('Enter your text: ')
string = 'restart'
#second variable
new_string = string[0]
#change the 'r' character to the penultimate '$' character
string = string.replace(new_string, '$')
string = new_string + string[1:]
#output
print(string)