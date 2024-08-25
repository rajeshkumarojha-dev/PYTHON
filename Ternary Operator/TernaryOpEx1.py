a = input('Enter any value of a: ')
b = input('Enter any value of b: ')

result = a if a<b else b if b<a else 'Both are equal'

print('({},{})={}'.format(a,b,result))
