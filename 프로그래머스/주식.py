


pri = [2, 3, 4, 2, 3, 1 ,3 ,4 ,1, 2, 3, 4]
ans = []


for i in range(5):
    try:
          while True:
            set = pri.pop(0) -1
            r = pri.index(set) +1
            ans.append(r)
    except:
         ans.append(len(pri))
    if ans[-1] == 0:
        break



print(ans)






