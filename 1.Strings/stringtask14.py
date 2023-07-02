"""Write a Python program that accepts a comma-separated sequence of words
as input and prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
#input variable
#string = input("Enter your text: ")
string = "red, black, pink, green"
#second variable with string division
new_string = [word for word in string.split(",")]
#output with combining rows into a list and putting the sets in ascending order 
print(",".join(sorted(list(set(new_string)))))