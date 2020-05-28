
arr = '()(((()())(())()))(())'



def solution(arr):
    Aist = list(arr)
    k,ans = 0,0
    for i in range(len(Aist)):
           if Aist[i] == '(' and Aist[i+1] != ')':
                   k +=1
                   ans +=1
           if Aist[i] == ')' and Aist[i-1] != '(':
                   k -=1
           if Aist[i] == '(' and Aist[i+1] == ')' and k != 0:
                   ans +=k

    return ans


