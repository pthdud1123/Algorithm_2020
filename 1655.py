import sys
import heapq

N=int(sys.stdin.readline())
maxheap=[]
minheap=[] #기준 값은 여기에 있어야 함

for i in range(N):
    d=int(sys.stdin.readline())
    if i ==0:
        heapq.heappush(minheap,d)
    else:
        if d >= minheap[0]:
            heapq.heappush(minheap,d)
        else:
            heapq.heappush(maxheap,(-d,d))
    if len(minheap)>len(maxheap)+1:
        temp=heapq.heappop(minheap)
        heapq.heappush(maxheap,(-temp,temp))
    elif len(minheap)<len(maxheap):
        heapq.heappush(minheap,heapq.heappop(maxheap)[1])

    if len(maxheap)==len(minheap):
        if maxheap[0][1]<=minheap[0]:
            print(maxheap[0][1])
        else:
            print(minheap[0])
    else:
        print(minheap[0])

