import heapq
import sys

N=int(sys.stdin.readline())
absheap=[]
for n in range(N):
    o=int(sys.stdin.readline())
    if o==0:
        if not absheap:
            print(0)
        else:
            print(heapq.heappop(absheap)[1])
    else:
        heapq.heappush(absheap,(abs(o),o))