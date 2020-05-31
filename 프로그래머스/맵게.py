import heapq



def solution(sco,k):

    heapq.heapify(sco)
    try:
        for i in range(1000000):
            if sco[0] < k:
                val = heapq.heappop(sco) + 2 * (heapq.heappop(sco))
                heapq.heappush(sco, val)
                ans = i + 1
            else:
                break
    except:
        ans = -1

    return ans

