


def solution(arr):
    arr = arr.replace('()', 'L')
    Aist = list(arr)
    k,ans = 0,0
    for i in range(len(Aist)):
           if Aist[i] == '(':
               k +=1
               ans =+1
           if Aist[i] == "L":
               ans+=k
           if Aist[i] == ')':
               k -=1

    return ans

