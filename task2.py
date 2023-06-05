string = 'Python is simple and effective!'
#input string
longest_word = max(string.split(' '), key=len)
#split a string into words separated by a space key len looking for the largest element of the string
print(longest_word)
#screen output