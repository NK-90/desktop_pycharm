arr = '()(((()())(())()))(())'
Aist = list(arr)
Zist = [z for z in range(len(Aist))]
Bist = []


k = 0
for i in range(12):
    while Aist[i] == "(" and Aist[i+1] == ")":
          k +=1
          Aist.pop(i-2*(k-1))
          Aist.pop(i-2*(k-1))
          break

# ['(', '(', '(', ')', '(', ')', ')', ')', '(', ')']
# ['(', '(', '(', ')', '(', ')', ')', ')', '(', '(', ')', ')']
# ['(', '(', '(', '(', ')', ')', '(', ')', ')', ')', '(', '(', ')', ')']
print(Aist)




print(Aist)