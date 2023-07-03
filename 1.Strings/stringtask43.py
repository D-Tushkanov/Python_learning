"""Write a Python program to print the square and cube symbols in
the area of a rectangle and the volume of a cylinder.
Sample output:
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3"""
#input first variable
area = 1256.66
#input second variable
volume = 1254.725
#the degree of the first variable
decimals = 2
#output with the first variable raised to a degree
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
#the degree of the second variable
decimals = 3
#output with the second variable raised to a degree
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))