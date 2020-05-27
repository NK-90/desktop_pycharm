Aist = ['(', ')', '(', '(', '(', '(', ')', '(', ')', ')', '(', '(', ')', ')', '(', ')', ')', ')', '(', '(', ')', ')']
Zist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
Bist = []
A_len = len(Aist)
Cist = []

for i in range(A_len) :
    if Aist[i] == '(':
        Bist.append(('a',Zist[i]))
    if Aist[i] == ')':
        Bist.append(('b',Zist[i]))


for i in range(A_len):
    if Bist[i][0] == 'a'and Bist[i+1][0] == 'b':
        Cist.append((,))