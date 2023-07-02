"""Write a Python program to reverse words in a string. """
#input variable
string = input("Enter your text: ")
#variable with word permutation
new_string = string.split()[::-1]
#appending  words to word
word = []
for i in new_string:
    word.append(i)
#output
print(" ".join(word))