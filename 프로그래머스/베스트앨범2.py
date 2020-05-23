geres =  ['classic','soul','classic','pop','classic', 'soul','soul']
plays =  [400       , 600 ,  500,     600 , 500 ,  100  , 100]


r_list = ['pop', 'classic', 'soul']




n_list = []
for val1 in r_list:
    temp = []
    for idx,val2 in enumerate(geres):
         if val1 == val2:
             temp.append(plays[idx])

    k = sorted(temp, reverse=True)
    print(k,val1)
    if len(k) == 1:
        s1 = k[0]   #600

        for i in range(len(geres)):
            if geres[i] == val1 and plays[i] == s1:
                answer.append(i)
                break

    else:
        s1 = k[0]
        s2 = k[1]



        if s1 == s2:
            for i in range(len(geres)):
                if geres[i] == val1 and plays[i] == s1:
                    answer.append(i)
                    continue
                if geres[i] == val1 and plays[i] == s1:
                    answer.append(i)
                    break

        else:
            for i in range(len(geres)):
                if geres[i] == val1 and plays[i] == s1:
                    answer.append(i)
                    break

            for i in range(len(geres)):
                if geres[i] == val1 and plays[i] == s2:
                    answer.append(i)
                    break

