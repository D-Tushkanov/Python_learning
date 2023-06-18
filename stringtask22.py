"""Write a Python program to sort a string lexicographically"""
#input variable
string = input("Enter your text: ")
#variable output with lexicographic sorting
print(sorted(string, key=str.upper))