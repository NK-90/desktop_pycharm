# b_len = 4
# weight = 10
# trucks = [6,2,5,6]



 # i       bridge        trucks
# i=0     [0,0,0,0]    [6,2,5,6]
# i=1 :   [0,0,0,6]    [2,5,6]
# i=2 :   [0,0,6,2]    [5,6]
# i=3 :   [0,6,2,0]    [5,6]
# i=4 :   [6,2,0,0]    [5,6]
# i=5 :   [2,0,0,5]    [6]
# i=6 :   [0,0,5,0]    [6]
# i=7 :   [0,5,0,0]    [6]
# i=8 :   [5,0,0,0]    [6]
# i=9 :   [0,0,0,6]    [ ]
# i=10:   [0,0,6,0]    [ ]
# i=11:   [0,6,0,0]    [ ]
# i=12:   [6,0,0,0]    [ ]
# i=13:   [0,0,0,0]    [ ]


def solution(b_len, weight, trucks):
    bridge = [0] * b_len
    b_sum = 0
    for i in range(1,2000000,1):
         bridge.pop(0)
         if b_sum +trucks[0] <= weight:
            bridge.append(trucks.pop(0))
            b_sum -= bridge[0]
            b_sum += bridge[-1]
         else:
            bridge.append(0)
            b_sum -= bridge[0]
         if len(trucks) == 0:
             i += b_len
             break

    return i



















# while sum(temp) + trucks[0] <= 10:
#     temp.append(trucks.pop(0))


