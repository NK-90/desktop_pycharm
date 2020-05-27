arr = '()(((()())(())()))(())'
arr = arr.replace('()','L')




Aist = list(arr)
Zist = [z for z in range(len(Aist))]
print(Aist)
print(Zist)
Bist =[]


Aist =  ['L', '(+1', '(+1', '(+1', 'L', 'L', ')-1', '(+1', 'L', ')-1', 'L', ')-1', ')-1', '(', 'L', ')']
Aist =  ['L', '(', '(', '(', 'L', 'L', ')', '(', 'L', ')', 'L', ')', ')', '(', 'L', ')']

k=0
for i,v in enumerate(Aist):
    if v == '(':
        k +=1
    if v == ')':
        k -=1
    if k == 0:
        Zist.pop(i)
        Zist.