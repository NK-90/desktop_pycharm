arr = '()(((()())(())()))(())'


Aist = list(arr)
Zist = [z for z in range(len(Aist))]
Bist = []
Cist = []
Dist = []
Eist = []
k = 0

print(Zist)

for i in range(len(Aist)):
    if  Aist[i] == "(" and Aist[i+1] == ")":
        k +=1
        Bist.append(i-2*(k-1))

for i in Bist:
    Aist.pop(i)
    Aist.pop(i)
    Cist.append(Zist.pop(i))
    Cist.append(Zist.pop(i))

Bist=[]



print(Aist)
print(Zist)
