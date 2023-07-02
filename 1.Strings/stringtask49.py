"""Write a Python program to count and display vowels in text."""
#input variable
string = input("Enter your text: ")
#output with vowel counting
print(*map(string.count, "aeiou"))
