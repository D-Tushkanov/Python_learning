def find_longest_word(s:str)->str:
    longest_word = max(s, key=len)
    return longest_word
x = 'Python is simple and effective!'
p = x.split(' ')
print(find_longest_word(p))
