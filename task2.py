s = 'Python is simple and effective!'
def find_longest_word(s:str)->str:
    max(s.split(), key=len)