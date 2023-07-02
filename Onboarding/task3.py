""""Implement a function that receives a string and replaces all " symbols with ' and vice versa."""


#create a variable for data input
text = input("Enter your text: ")
#initial value of the variable for the result
replaced_string = ""
#cycle start
for char in text:
    #cycle conditions
    #if the char in the text has a double quote, then change it to a single quote
    if char == "'":
        replaced_string += '"'
    #if the char in the text has a single quote, then change it to a double quote
    elif char == '"':
        replaced_string += "'"
    #else the character is not a quotation mark, leave it as it is
    else:
        replaced_string += char
        
print(replaced_string)