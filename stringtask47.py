"""Write a Python program to lowercase the first n characters in a string"""
#input variables
string = input("Enter your text: ")
n = int(input("Enter your number: "))
newstring = ""

for i in range(0, n):
    #conversion to small characters
    newstring += string[i].lower()
    #conversion into small characters of a n-th numb
newstring += string[n:]
#output
print(newstring)