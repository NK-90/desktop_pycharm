


pri = [2, 3, 2, 0, 1, 3, 1]



def solution(pri):


    ans = []
    check =0
    for i,v in enumerate(pri):
        for j in range(i+1,len(pri),1):
            check =0
            if v > pri[j]:
                ans.append(j-i)
                check +=1
                break
        if check == 0:
            ans.append(len(pri)-i-1)

    if len(ans) != len(pri):
        ans.append(0)
    return ans

solution(pri)











