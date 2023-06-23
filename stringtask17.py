"""Write a Python function to get a string made of 4 copies of
the last two characters of a specified string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses"""
#input variables
string = "Python"
second_string = "Exercises"
#variables where we take the last two characters and multiply by four
new_string = string[-2:]*4
new_string_two = second_string[-2:]*4
#output variables with changes
print(new_string)
print(new_string_two)
