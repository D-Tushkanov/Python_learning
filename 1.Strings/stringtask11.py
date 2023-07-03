"""Write a Python program to remove characters that
have odd index values in a given string"""

#input variable
string = input("Enter your text: ")
#output variable
new_string = ''
#sequence and length of characters
for i in range(len(string)):
    #if find an even divide by two
    if (i % 2 == 0):
        #every second character
        new_string = new_string + string[i]
#output
print(string)
print(new_string)