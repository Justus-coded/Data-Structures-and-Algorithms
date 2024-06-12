import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        # for i in range(len(stones)):
        #     stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first: #first != second:
                heapq.heappush(stones, first - second)

        if stones:
            return abs(stones[0])
        else:
            return 0


stones = [2,3,6,2,4]#[2,7,4,1,8,1]
sol = Solution()
print(sol.lastStoneWeight(stones))
        