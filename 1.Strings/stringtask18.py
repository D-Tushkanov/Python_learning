"""Write a Python function to get a string made of the first three characters of a specified string.
If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt"""
#input variable
string = input("Enter your text: ")
#get First 3 character of a string
char = string[0:3]
#output
print('First 3 character : ', char)