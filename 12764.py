import sys
import heapq

N=int(sys.stdin.readline())
time=[tuple(map(int,sys.stdin.readline().split()))for _ in range(N)]
time.sort()

count=[0 for _ in range(N)]
lasttime=[0 for _ in range(N)]
emptyseat=[]# 번호
heap=[]
num=0

for start,last in time:
    while heap:
        if start >= heap[0][0]:
            heapq.heappush(emptyseat,heapq.heappop(heap)[1])
        else :
            break

    if emptyseat:
        number=heapq.heappop(emptyseat)
        count[number]+=1
        lasttime[number]=last
        heapq.heappush(heap,(last,number))
    else:
        count[num]+=1
        lasttime[num]=last
        heapq.heappush(heap,(last,num))
        num+=1



print(num)
for i in range(num):
    print(count[i],end=" ")
