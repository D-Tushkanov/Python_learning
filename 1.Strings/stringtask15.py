"""Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'"""
#first variable
string = 'Python'
#second variable
tag = 'i'
#third variable
new_string = "<>"
#fourth variable
slash = "/"
#variable concatenation
modified_string = new_string[:1] + tag + new_string[1:] + string + new_string[:1]\
                  + slash + tag + new_string[1:]
#output
print(modified_string)