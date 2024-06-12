from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,9]

sol = Solution()
print(sol.hasDuplicate(num))