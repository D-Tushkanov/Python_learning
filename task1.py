""""Fractions
Create a function that takes two parameters of string type which are fractions with the same denominator
and returns a sum expression of these fractions and the sum result.
For example:
>>> a_b = '1/3'
>>> c_b = '5/3'
>>> get_fractions(a_b, c_b)
'1/3 + 5/3 = 6/3'"""

a_c = '1/3'
b_c = '5/3'
sum = int(a_c.split('/')[0])+int(b_c.split('/')[0])
print(a_c + '+' + b_c + '=' + str(sum) + '/' + a_c.split('/')[1])