List = [1, 1, 9, 1, 1, 1]
# Zist = [0, 1, 2, 3, 4, 5]
location = 3


def solution(List,location):
    Zist = [x for x in range(len(List))]
    Aist = []

    for j in range(1000):
        if List[0] == max(List):
            List.pop(0)
            Aist.append(Zist.pop(0))
            if len(List) == 0:
                break
        else:
            List.append(List.pop(0))
            Zist.append(Zist.pop(0))

    print(Aist.index(location))
    return Aist.index(location) + 1


solution(List,location)