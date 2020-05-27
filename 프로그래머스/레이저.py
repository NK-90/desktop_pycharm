
arr = '()(((()())(())()))(())'


def solution(arr):


        ans = 0
        Zist = [z for z in range(len(list(arr.replace('()','L'))))]
        Cist = []
        Dist = []


        Wist = [z for z in [z for z in range(len(list(arr.replace('()','L'))))] if list(arr.replace('()','L'))[z] == 'L' ]
        Bist = [i for i in list(arr.replace('()','L')) if i != 'L']
        for i in Wist:
            Zist.remove(i)


        for i in range(200):
            i = -1
            try:
                while True:
                    i +=1
                    if Bist[i] == '('and  Bist[i+1] == ')':
                        Cist.append((Zist[i],Zist[i+1]))
                        Dist.append((Zist[i],Zist[i+1]))
            except:
                pass


            for i in range (len(Cist)):
              Zist.remove(Cist[i][0])
              Zist.remove(Cist[i][1])
            Cist =[]
            Bist = [b for b in  list(''.join(Bist).replace('()','L')) if b != 'L']



        ans += len(Dist)
        for i in range(len(Wist)):
            for j in range(len(Dist)):
               if Dist[j][0] < Wist[i] and Wist[i] < Dist[j][1]:
                   ans +=1

        print(ans)
        return ans
