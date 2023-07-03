"""Write a Python program to find the first appearance of
the substrings 'not' and 'poor' in a given string.
If 'not' follows 'poor', replace the whole 'not'...'poor' substring
with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'"""
#input variable
string = input("Enter your text: ")
#word search not
not_find = string.find('not')
#word search poor
poor_find = string.find('poor')
#If the word not comes before the word poor, then both words are changed to the word good
if not_find < poor_find and not_find != -1:
    modified_string = string[:not_find] + 'good' + string[poor_find+4:]
else:
    modified_string = string
#output modified string
print(modified_string)
