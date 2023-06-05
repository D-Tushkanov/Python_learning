#create a variable for entering text
cleaned_string = input("Enter your text: ")
#create a method that combines the entered characters without spaces and with small letters,
#and create a method to check if the given string consists only of letters and numbers
cleaned_string = ''.join(c.lower() for c in cleaned_string if c.isalnum())
#create a variable for entering text
length = len(cleaned_string)
#create a loop that divides the entered text by two without a remainder
for i in range(length // 2):
    #compare the characters first and last, second and penultimate, and so on to the central, it remains unchanged
    if cleaned_string[i] != cleaned_string[length - i - 1]:
        #if the characters don't match
        print("String is not palyndrome!")
        break
#if the characters match
print("String is palyndrome!")