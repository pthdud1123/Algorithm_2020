import heapq
import sys

N=int(sys.stdin.readline())
heap=[]
for i in range(N):
    input=list(map(int,sys.stdin.readline().split()))
    heapq.heapify(input)
    if heap:
        for j,w in enumerate (input):
            h=heapq.heappop(heap)
            if h<w:
                heapq.heappush(heap,w)
            else:
                heapq.heappush(heap,h)
    else:
        for j,w in enumerate(input):
            heap=input
print(heapq.heappop(heap))
