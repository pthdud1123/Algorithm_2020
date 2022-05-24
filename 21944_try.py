import sys
import heapq
from collections import defaultdict

N=int(sys.stdin.readline())
minheap=[]
maxheap=[]
solve=defaultdict(bool)

for i in range(N):
    P,L,G=map(int,sys.stdin.readline().split())
    heapq.heappush(maxheap,(-L,-P,G))
    heapq.heappush(minheap,(L,P,G))
    solve[P]=True

M=int(sys.stdin.readline())
for i in range(M):
    command=sys.stdin.readline().split()
    if command[0] == "recommend":
        while minheap and not solve[minheap[0][1]]:
            heapq.heappop(minheap)
        while maxheap and not solve[-maxheap[0][1]]:
            heapq.heappop(maxheap)
        min=minheap.copy()
        max=maxheap[:]
        g,x=int(command[1]),int(command[2])
        if x==1:
            while max[0][2]!=g:
                heapq.heappop(max)
            print(-max[0][1])
        elif x==-1:
            while min[0][2]!=g:
                heapq.heappop(min)
            print(min[0][1])

    if command[0] =="recommend2":
        x=int(command[1])
        while minheap and not solve[minheap[0][1]]:
            heapq.heappop(minheap)
        while maxheap and not solve[-maxheap[0][1]]:
            heapq.heappop(maxheap)
        min = minheap.copy()
        max = maxheap[:]
        if x==1:
            print(-max[0][1])
        elif x==-1:
            print(min[0][1])

    if command[0] =="recommend3":
        x,l=int(command[1]),int(command[2])
        while minheap and not solve[minheap[0][1]]:
            heapq.heappop(minheap)
        while maxheap and not solve[-maxheap[0][1]]:
            heapq.heappop(maxheap)
        min = minheap.copy()
        max = maxheap[:]
        if x == 1:
            while min and(not min[0][0] >= l or not solve[min[0][1]]):
                heapq.heappop(min)
            if min:
                print(min[0][1])
            else:
                print("-1")
        elif x ==-1:
            while max and(not -max[0][0]<l or not solve[-max[0][1]]):
                heapq.heappop(max)
            if max:
                print(-max[0][1])
            else:
                print("-1")

    if command[0] == "add":
        while minheap and not solve[minheap[0][1]]:
            heapq.heappop(minheap)
        while maxheap and not solve[-maxheap[0][1]]:
            heapq.heappop(maxheap)
        p,l,g=int(command[1]),int(command[2]),int(command[3])
        heapq.heappush(minheap,(l,p,g))
        heapq.heappush(maxheap,(-l,-p,g))

    if command[0] =="solved":
        p=int(command[1])
        solve[p]=False