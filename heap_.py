import heapq

#a = [1, 2, 3, 5, 6, 8, 7]
a ={1:3, 2:5, 3:2, 5:1, 6:4, 8:6, 7:7}

b=list(a.values())
c= heapq.heapify(b)
d=heapq.heappop(c)

print(d)
#[2, 5, 3, 7, 6, 8]