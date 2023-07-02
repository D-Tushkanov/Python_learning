"""Write a Python program to change a given string to a newly string where
the first and last chars have been exchanged. """

#input variable
string = input('Enter your text: ')
#second variable for index search and character substitution
new_str = string[-1] + string[1:-1] + string[0]
#output
print(new_str)