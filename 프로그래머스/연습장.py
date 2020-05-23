heights = [3,9,9,3,5,7,2]

def solution(heights):
    ans = [0] * len(heights)
    for i in range(len(heights) - 1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                ans[i] = j+1
                break
    print(ans)
    return ans

solution(heights)

