arr = '()(((()())(())()))(())'
Aist = list(arr)



for i in range(len(Aist)):
    if i !=0 and Aist[i-1] == "(" and Aist[i] == ")":
        Aist.pop(i)
        Aist.pop(i-1)



print(Aist)

