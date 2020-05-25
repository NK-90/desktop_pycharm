pro = [93,30,40,55,30]
up  = [1,30,30,5,3]




Temp  = []
temp = []
ans   = []

for idx,val in enumerate(pro):
    n=0
    while val < 100:
       val += up[idx]
       n +=1
    Temp.append(n)

print(Temp)
k = Temp[0]
for idx,val in enumerate(Temp):
     temp.append(Temp.pop(0))
     if idx != 0:
       k = Temp[0]
     print(idx,k,Temp,temp,val)
     if k < val:
         print(idx,temp)
         ans.append(len(temp))
         temp= []



