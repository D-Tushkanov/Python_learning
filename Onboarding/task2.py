""""Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on).
If there are multiple longest words in the string with the same length return the word that occurs first.
Example:
>>> get_longest_word('Python is simple and effective!')
'effective!'"""

string = 'Python is simple and effective!'
#input string
longest_word = max(string.split(' '), key=len)
#split a string into words separated by a space key len looking for the largest element of the string
print(longest_word)
#screen output