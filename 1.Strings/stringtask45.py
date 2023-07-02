"""Write a Python program to check whether a string contains
 all letters of the alphabet"""
#python string module
import string
#set variable + constant
alphabet = set(string.ascii_lowercase)
#first input
input_string = 'the quick brown fox jumps over the lazy dog'
#first output checks for all letters of the alphabet
print(set(input_string) >= alphabet)
#second input
input_string = 'the quick brown fox jumps over the lazy cat'
#srcond output checks for all letters of the alphabet
print(set(input_string) >= alphabet)