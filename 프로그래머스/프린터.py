priorities = [1,1,2,3,1,1,1]

location = 4


def solution (priorities, location):

    Zist = [x for x in range(len(priorities))]
    k = max(priorities)

    for i in priorities:
        priorities.append(priorities.pop(0))
        Zist.append(Zist.pop(0))
        if priorities[0] == k:
            break


    answer = Zist.index(location) +1
    print(answer)
    return answer

solution(priorities,location)