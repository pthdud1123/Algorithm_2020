import heapq
import sys
N=int(sys.stdin.readline())
heap=[]
for n in range(N):
    o=int(sys.stdin.readline())
    if o==0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-o,o))
