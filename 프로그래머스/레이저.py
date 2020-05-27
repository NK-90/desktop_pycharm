
arr = '()(((()())(())()))(())'
arr = arr.replace('()','L')
Aist = list(arr)
Zist = [z for z in range(len(Aist))]
Cist = []
Dist = []


Wist = [z for z in Zist if Aist[z] == 'L' ]
Bist = [i for i in Aist if i != 'L']
for i in Wist:
    Zist.remove(i)



Bist = ['(', '(', '(', ')', '(', ')', ')', ')', '(', ')']
Zist = [ 1,   2,   3,   6,   7,   9,   11,  12,  13, 15 ]

for i in range(100):
    i=-1
    try:
        while True:
            i +=1
            if Bist[i] == '('and  Bist[i+1] == ')':
                Cist.append((Zist[i],Zist[i+1]))
                Dist.append((Zist[i],Zist[i+1]))
    except:
        pass


    for i in range (len(Cist)):
      Zist.remove(Cist[i][0])
      Zist.remove(Cist[i][1])
    Cist =[]
    Bist = [b for b in  list(''.join(Bist).replace('()','L')) if b != 'L']


print(Wist)
print(Dist)