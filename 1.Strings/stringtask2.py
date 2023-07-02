"""Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""

string = "google.com"
new_string = {}

for i in string:
    #if  characters in a row are the same, then + 1
    if i in new_string:
       new_string[i] += 1
    #if the characters in a row are unequal, then nothing
    else:
        new_string[i] = 1
#output
print('Result: ' + str(new_string))