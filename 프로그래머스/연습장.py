
Aist =  ['L', '(', '(', '(', 'L', 'L', ')', '(', 'L', ')', 'L', ')', ')', '(', 'L', ')']


try:
    for i in range(1000):
       Aist.remove('L')
except ValueError:
    pass

print(Aist)

