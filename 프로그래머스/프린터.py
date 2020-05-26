List = [1, 1, 9, 1, 1, 1]
location = 0


def solution(List,location):
    Zist = [x for x in range(len(List))]
    Aist = []



    for i in range(10000):

        for j in List:
            List.append(List.pop(0))
            Zist.append(Zist.pop(0))
            if List[0] == max(List):
                List.pop(0)
                Aist.append(Zist.pop(0))

        if len(Zist) == 0:
            break
    print(Aist)
    print(Aist.index(location)+1)
    return Aist.index(location)+1


solution(List,location)