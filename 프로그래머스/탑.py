# heights = [3,9,9,3,5,7,2]



def solution(heights):

    reights = list(reversed(heights))
    answer=[0] * len(heights)

    for i,val1 in enumerate(heights):
        for j,val2 in enumerate(reights[len(heights)-i:]):
            if val2 > val1:
                answer[i] = (len(reights[len(heights)-i:])-j)
                break

    print(answer)
    return answer

