b_len = 4
weight = 10
trucks = [6,2,5,6]
bridge = [0] * b_len



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



for i in range(1,2000,1):
    bridge.pop(0)
    if    sum(bridge) + trucks[0] :
        bridge.append(trucks.pop(0))
    elif  sum(bridge) + trucks[0] :
       bridge.append(0)



