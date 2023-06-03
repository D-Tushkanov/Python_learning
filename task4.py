#first variable
text = input('Enter your text: ')
#second variable
new_text = ""
#create a cycle of sequence enumeration
for i in text:
#cycle body
    new_text = i + new_text
#cycle conditions
if (text == new_text):
    print("Yes")
else:
    print("No")