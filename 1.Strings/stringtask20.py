"""Write a Python function to reverse a string if its length is a multiple of 4."""
#input variable
string = input("Enter your text: ")
#we divide with no remainder by four
if(len(string)%4 == 0):
    #output if four characters
    print(string[::-1])
else:
    #output if not four characters
    print("length is not equal to 4")