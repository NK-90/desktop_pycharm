


pri = [1, 2, 3, 2, 3]
ans = []

# i v
# 0 1
# 1 2
# 2 3
def solution(pri):
    ans = []
    for i in range(len(pri)):
        temp = pri.pop(0)
        k=0
        for j in pri:
            k+=1
            if temp >  j:
                ans.append(k)
                break
            elif k == len(pri):
                ans.append(k)

    ans.append(0)
    return ans