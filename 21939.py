import sys
import heapq
from collections import defaultdict

N=int(sys.stdin.readline())
minheap=[]
maxheap=[]
visited=defaultdict(bool)
for i in range(N):
    p,l=map(int,sys.stdin.readline().split())
    heapq.heappush(minheap,(l,p))
    heapq.heappush(maxheap,(-l,-p))
    visited[p]=True


M=int(sys.stdin.readline())
for i in range(M):
    command=sys.stdin.readline().split()
    j=len(visited)
    if command[0] == 'add':
        p = int(command[1])
        l = int(command[2])
        while not visited[-maxheap[0][1]]:
            heapq.heappop(maxheap)
        while not visited[minheap[0][1]]:
            heapq.heappop(minheap)
        heapq.heappush(minheap,(l,p))
        heapq.heappush(maxheap,(-l,-p))
        visited[p]=True

    if command[0] == 'recommend':
        p = int(command[1])
        if p==1:
            while not visited[-maxheap[0][1]]:
                heapq.heappop(maxheap)
            print(-maxheap[0][1])
        else:
            while not visited[minheap[0][1]]:
                heapq.heappop(minheap)
            print(minheap[0][1])

    if command[0] == 'solved':
        p = int(command[1])
        visited[p]=False

