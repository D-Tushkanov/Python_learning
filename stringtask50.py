"""Write a Python program to split a string on
the last occurrence of the delimiter."""
#input variable
string = input('Enter your text, separated by commas: ')
#second variable with rindex
new_string = string.rindex(',')
#0 index second variable
string1 = string[0:new_string]
#last word in second variable
string2 = string[new_string+1::]
#output
print(string1)
print(string2)