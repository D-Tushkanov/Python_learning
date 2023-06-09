""""Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String """

string = "w3resource"
count = 0
#the number of repetitions of the specified value in the string
for i in string:
    count = count + 1
#index summation
new_string = string[0:2] + string[count - 2: count]
#output
print("Input string = " + string)
print("New String = " + new_string)
