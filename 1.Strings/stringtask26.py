"""Write a Python program to display formatted text (width=50) as output"""
#text formatting module
import textwrap
#input variable
string = input('Enter your text: ')
#output with 50 wide text formatting
print(textwrap.fill(string, width=50))
