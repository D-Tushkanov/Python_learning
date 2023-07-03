"""Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}"""
#first variable
string = 'Python'
#second variable
new_string = '[[]]'
#the concatenation variable of the first and second variables
modified_string = new_string[:2] + string + new_string[2:]
#output
print(modified_string)

