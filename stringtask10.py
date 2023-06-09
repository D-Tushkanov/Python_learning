#input variable
string = input('Enter your text: ')
#second variable for index search and character substitution
new_str = string[-1] + string[1:-1] + string[0]
#output
print(new_str)