"""Write a Python program to remove existing indentation from all of the lines in a given text"""
import textwrap
#string = input('Enter your text: ')
#first variable
string = """
         Cinderella is one of the best-known English stories, 
         and it is often used to help people learn English. 
         The story is about a young girl who is treated badly by her stepmother and stepsisters. 
         But with the help of her fairy godmother, she attends a royal ball and meets the prince. 
         With a little help from her friends, she manages to win the prince’s heart and lives happily ever after. 
         The story is full of fun and adventure, and it is a great way to improve English language skills.
         """
#output first variable
print(string)
#create second variable in which we align the string
modified_string = textwrap.dedent(string)
#output second variable
print(modified_string)