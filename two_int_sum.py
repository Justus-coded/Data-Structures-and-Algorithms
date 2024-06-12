from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans =[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
        return ans

### solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ### Using Hashmap
        ## map val to index
        map = {} # val : index

        for i , n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return
