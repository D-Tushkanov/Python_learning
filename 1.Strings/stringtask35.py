"""Write a Python program to display a number with a comma separator. """
#input first variable
first_number = int(input('Enter first number: '))
#input second variable
second_number = int(input('Enter second number: '))
#output first variable
print("Original Number: ", first_number)
#output first variable with changes
print("Formatted Number with comma separator: "+"{:,}".format(first_number))
#output second variable
print("Original Number: ", second_number)
#output second variable with changes
print("Formatted Number with comma separator: "+"{:,}".format(second_number))
