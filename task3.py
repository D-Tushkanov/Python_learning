text = input('Enter your text: ')
new_text = ''
for i in text:
    if i in text:
        pimp = text.replace('\"', "\'")
    else:
        pimp = text.replace("\'", '\"')
print(pimp)