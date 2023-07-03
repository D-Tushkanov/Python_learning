"""Write a Python program to count the occurrences of each word in a given sentence"""

#input variable
string = input('Enter your text: ')
#split the line
string = string.split()
#variable for sequences and translation into a list
new_string = list(set(string))
for i in new_string:
    #output with the total number of repetitions
    print(i, "-", string.count(i))
