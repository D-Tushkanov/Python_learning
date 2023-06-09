"""Write a Python program to remove the nth index character from a nonempty string"""

string = input('Enter your text: ')
removed_string = int(input("Enter your index: "))
output_string = ''
#string length
if removed_string < len(string):
    #function for finding the minimum and maximum values in a numeric sequence
    for i, char in enumerate(string):
        #variable comparison
        if i == removed_string:
            continue
        output_string += char
    #output
    print(output_string)
else:
    print('You entered invalid index!')