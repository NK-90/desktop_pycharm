b_len = 4
weight = 10
truck_weights = [7,4,5,6]



b_list = [0] * b_len


# i=0      [0,0,0,0] [7,4,5,6]
# i=1 :    [0,0,0,7] [4,5,6]
# i=2 :    [0,0,7,0] [4,5,6]
# i=3 :    [0,7,0,0] [4,5,6]
# i=4 :    [7,0,0,0] [4,5,6]
# i=5 :    [0,0,0,4] [5,6]

run = truck_weights.pop(0)

def passing():
    for i in range(b_len):
        b_list[b_len - i-1] = run
        if i >0:
            b_list[b_len-i] = 0

    print(b_list)
    return

passing()