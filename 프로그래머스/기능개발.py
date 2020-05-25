pro = [93,30,40,55,30,93,30,40]
up  = [1,30,30,5,30,1,30,30]



def solution(pro,up):
    Temp  = []
    temp = []
    ans   = []

    for idx,val in enumerate(pro):
        n=0
        while val < 100:
           val += up[idx]
           n +=1
        Temp.append(n)


    k = Temp.pop(0)
    temp.append(k)

    for i in range(len(Temp)):
        if k >= Temp[0]:
            temp.append(Temp.pop(0))
        elif k < Temp[0]:
            ans.append((len(temp)))
            temp.clear()
            k = Temp.pop(0)
            temp.append(k)

    ans.append(len(temp))


    return ans

