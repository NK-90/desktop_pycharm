
arr = '()(((()())(())()))(())'



def solution(arr):

        arr = arr.replace('()','L')
        Zist = [z for z in range(len(arr))]
        Qist1 =[]
        Qist2 =[]
        ans = 0

        Wist  = [i for i in Zist if arr[i] =='L']
        Zist = [i for i in Zist if arr[i] !='L']
        Aist  = [x for x in arr if x != 'L']




        Aist = ['(', '(', '(', ')', '(', ')', ')', ')', '(', ')']
        Zist = [ 1,   2 ,  3,   6,   7,   9,  11,  12,   13, 15 ]

        for i in range(10000):
            i = -1
            try:
                while i < 2:
                    i+=1
                    if Aist[i] == '(' and Aist[i+1] == ')':
                            Aist.pop(i)
                            Aist.pop(i)
                            Qist1.append(Zist.pop(i))
                            Qist2.append(Zist.pop(i))
                            i-=1
            except:
                pass
            if len(Aist) == 0:
                break




        for i in range(len(Qist1)):
             for j in Wist:
                if Qist1[i] < j < Qist2[i]:
                    ans+=1
        ans += len(Qist1)

        return ans
