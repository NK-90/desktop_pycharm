pro = [93,30,55]
up  = [1,30,5]




temp = []
ans = []

for idx,val in enumerate(pro):
    n=0
    while val < 100:
       val += up[idx]
       n +=1
    temp.append(n)
    print(idx,temp)
    if temp[0] < temp[-1]:
        ans.append(len(temp) - 1)
        temp = [temp[-1]]
print(ans)


