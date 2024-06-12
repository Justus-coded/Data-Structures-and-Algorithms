import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        for i in range(k-1):
            heapq.heappop(nums)
            

        return abs(nums[0])
    

nums = [2,3,1,1,5,5,4]
k = 3
sol = Solution()

print(sol.findKthLargest(nums, k))

        