"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing', add 'ly' instead. If the string length of
the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""
#create variable
string = input('Enter your text: ')
#conditions if the string is less than three
if len(string) >= 3:
    #if string >= 3, + 'ing'
    if string.endswith('ing'):
        #if you enter ing, + 'ly'
        string += 'ly'
    else:
        string += 'ing'
#output
print(string)