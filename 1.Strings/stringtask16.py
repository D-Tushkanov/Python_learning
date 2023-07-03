string = input('Enter your text: ')
new_string = string
changed_string = modifield_string = 0
changed_string = string.find('not')
modifield_string = string.find('poor')
print(changed_string, modifield_string)
if (changed_string >= 0 and modifield_string >= 0):
    new_string = new_string.replace(new_string[changed_string:modifield_string],'good', 4)
print(new_string)