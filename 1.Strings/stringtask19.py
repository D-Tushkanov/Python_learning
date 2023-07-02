"""Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python"""
#input variable
string = 'https://www.w3resource.com/python-exercises/string'
#output with a line separator
print(string.rsplit('/', 1)[0])
print(string.rsplit('-', 1)[0])