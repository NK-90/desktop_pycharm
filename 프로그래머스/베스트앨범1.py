geres = ['classic','pop','classic','pop','classic','classic','soul','soul','soul']
plays = [400,       600,   150,     2500, 500,      500     , 500  , 100  , 100]



def solution(geres,plasys):




    s_list = sorted((set(geres)))
    m_list = []
    r_list = []
    n_list = []
    answer = []

    for j,gen_ls in enumerate(s_list):
        k = 0
        for i, gen in enumerate(geres):
            if gen == gen_ls:
                 k += plays[i]
        m_list.append(k)


    for i in range(len(s_list)):
        idx = m_list.index(max(m_list))
        m_list.remove(max(m_list))
        r_list.append(s_list.pop(idx))





    for val1 in r_list:
        temp = []
        for idx,val2 in enumerate(geres):
             if val1 == val2:
                 temp.append(plays[idx])

        k = sorted(temp, reverse=True)
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

    return answer


