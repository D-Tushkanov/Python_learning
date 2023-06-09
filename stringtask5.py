"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""
#input variable
string = input('Enter your text: ')
string_two = input('Enter your text: ')
string_three = ' '
#character substitution
new_string = string.replace('c', 'z')
new_string_two = string_two.replace('z', 'c')
#output
print(new_string_two + string_three + new_string)