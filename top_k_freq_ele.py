from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        freq_count = Counter(nums)
        
        # Sort the numbers based on their frequency in descending order
        sorted_nums = sorted(freq_count.keys(), key=lambda x: freq_count[x], reverse=True)
        
        # Return the top k frequent numbers
        return sorted_nums[:k]
    

#class Solution:
def topKFrequent(nums: List[int], k: int) -> List[int]:
    map = {}
    for i in nums:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    ##sort the values of map from highest to lowest and return the top k
    #return sorted(map.values())[:k]

    # Sort the numbers based on their frequency in descending order
        sorted_nums = sorted(map.keys(), key=lambda x: map[x], reverse=True)
    
    # Return the top k frequent numbers
    return sorted_nums[:k]



def topKFrequent_(nums, k):
    # Count the frequency of each element
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Use a heap to get the k most frequent elements
    # We use a min-heap with negative frequencies to simulate a max-heap
    max_heap = []
    for num, freq in frequency.items():
        heapq.heappush(max_heap, (-freq, num))  # Push negative frequency to simulate max heap

    # Extract the top k elements
    result = []
    for _ in range(k):
        result.append(heapq.heappop(max_heap)[1])  # The second item in the tuple is the element

    return result



# Test cases
nums = [1,1,1,2,2,5,4,5,5,3]
k = 3

# Expected output: [1, 2]
print(Solution().topKFrequent(nums, k))

print(topKFrequent_(nums, k))