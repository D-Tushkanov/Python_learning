""""Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String """
#input variable
string = input('Enter your text: ')
new_string = ''
if len(string) >= 2:
    #cut two symbols on each side
    new_string = string[:2] + string[-2:]
    print(new_string)
else:
    print('Empty String')
