"""Write a Python program to convert a given string into a list of words.
Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']"""
#input variable
string = input('Enter your text: ')
#convert the string into a list
string = string.split(',')
#output
print(string)