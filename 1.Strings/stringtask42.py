"""Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
                o 4
                e 3
                u 2
                h 2
                r 2
                t 2"""
#input variable
string = input("Enter your text: ")
#dictionary or set
new_string = {}
for i in string:
    if i in new_string:
        new_string[i] += 1
    else:
        new_string[i] = 1
#output
print(new_string)