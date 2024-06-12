import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            
            dist = (x**2) + (y**2)
            minheap.append(dist,x,y)

        heapq.heapify(minheap)
        res =[]
        for _, x, y in range(k):

            _,x,y = heapq.heappop(minheap)
            res.append((x,y))
        return res
