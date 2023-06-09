"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""
string = 'abc'
string_two = 'xyz'
string_three = ' '
new_string = string.replace('c', 'z')
new_string_two = string_two.replace('z', 'c')
print(new_string_two + string_three + new_string)