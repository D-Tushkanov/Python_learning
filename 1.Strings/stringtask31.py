"""Write a Python program to print the following numbers up to 2 decimal places with a sign"""
#input variable
chislo = float(input())
#second variable + format
format_chislo = '{:+.2f}'.format(chislo)
#output
print(format_chislo)