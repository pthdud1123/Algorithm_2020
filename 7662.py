import heapq
import sys
T=int(sys.stdin.readline())
for t in range(T):
    K=int(sys.stdin.readline())
    max,min=[],[]
    check=[False]*K
    for k in range(K):
        o,n=sys.stdin.readline().split()
        if o == 'I':
            heapq.heappush(max,(-1*int(n),k))
            heapq.heappush(min,(int(n),k))
            check[k]=True
        else:
            if int(n) ==-1:
                while min and not check[min[0][1]]:
                    heapq.heappop(min)
                if min:
                    check[min[0][1]]=False
                    heapq.heappop(min)
            else:
                while max and not check[max[0][1]]:
                    heapq.heappop(max)
                if max:
                    check[max[0][1]]=False
                    heapq.heappop(max)

        while max and not check[max[0][1]]:
            heapq.heappop(max)
        while min and not check[min[0][1]]:
            heapq.heappop(min)

    if max and min:
        print(heapq.heappop(max)[0]*-1,heapq.heappop(min)[0])
    else:
        print("EMPTY")
