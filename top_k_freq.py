import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap ={}  #create an hashmap to store the number and frequency
        for i in nums:
            if i in hashmap: 
                hashmap[i] +=1  #if num in hashmap add one to occurence
            else:
                hashmap[i] = 1 #if num not in hashmap, set the freq to one

        maxheap =[]  # create as empty heap
        for num, freq in hashmap.items():  ## return the num and frequency
            heapq.heappush(maxheap, (-freq,num)) ## push to the heap, negative freq and number as a tuple

        result = [] ## initialize a bucket for results 
        for _ in range(k): ## loop through the k number of item req
            result.append(heapq.heappop(maxheap[1])) ## pop from the maxheap and append to result

        return result