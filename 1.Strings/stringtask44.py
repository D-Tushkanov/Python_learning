"""Write a Python program to print the index of a character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9"""
#input variable
string = input('Enter your text: ')
#string = "w3resource"
#item counter
for index, char in enumerate(string):
    #output
    print("Current character", char, "position at", index)