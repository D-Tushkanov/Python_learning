string = 'Python is simple and effective!'
#строка с входными данными
longest_word = max(string.split(' '), key=len)
#сплит разбивает строку на слова разделенные пробеломб кейлен ищет самый большой элемент строки
print(longest_word)
#вывод на экран