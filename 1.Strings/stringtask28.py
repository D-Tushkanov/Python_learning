"""Write a Python program to add prefix text to all of the lines in a string. """

#input variable
string = input("Enter your text: ")
#second variable
new_string = string.split('.')
#conditions
for i in new_string:
#output
    print(">"+i)