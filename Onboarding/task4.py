""""Write a function that checks whether a string is a palindrome or not.
The usage of any reversing functions is prohibited."""


#create a variable for entering text
cleaned_string = input("Enter your text: ")
'''

invoke a method that storing combination the entered characters without spaces and with small letters,
and invoke a method to check if the given string consists only of letters and numbers


'''
cleaned_string = ''.join(c.lower() for c in cleaned_string if c.isalnum())
#create a variable for entering text
length = len(cleaned_string)
#create a loop that divides the entered text by two pieces
for i in range(length // 2):
    #compare the characters between first and last up to center of the string
    if cleaned_string[i] != cleaned_string[length - i - 1]:
        #if any character don't match, get out of loop
        print("String is not palyndrome!")
        break
#if the characters match, end
print("String is palyndrome!")