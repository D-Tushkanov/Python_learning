"""Write a Python program to display a number in left,
right, and center aligned with a width of 10. """
#input variable
number = int(input())
#output
print("Left aligned (width 10)   :"+"{:< 10d}".format(number))
print("Right aligned (width 10)  :"+"{:10d}".format(number))
print("Center aligned (width 10) :"+"{:^10d}".format(number))
