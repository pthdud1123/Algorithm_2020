import sys
import heapq
import math

def solve(content):
    maxheap = []  # 기준 값이 있음
    minheap = []
    value = []
    for i, num in enumerate(content):
        if i == 0:
            heapq.heappush(maxheap, num)  # 처음 기준 값 삽입
        else:
            if num > maxheap[0]:  # 기준보다 크면 max heap에 넣어줌
                heapq.heappush(maxheap, num)
            else:
                heapq.heappush(minheap, (-num, num))
        # maxheap,minheap의 크기가 같거나, maxheap의 크가 같게 유지 해주어야함
        if len(maxheap) < len(minheap):
            data = heapq.heappop(minheap)
            heapq.heappush(maxheap, data[1])
        elif len(maxheap) > len(minheap) + 1:
            data = heapq.heappop(maxheap)
            heapq.heappush(minheap, (-data, data))
        if i % 2 == 0:  # 홀수일 때 중앙 값 출력
            value.append(maxheap[0])

    for i in range(len(value)):
        if i!=0 and (i+1)%10 == 1:
            print()
        print(value[i], end=' ')
    print()


T=int(sys.stdin.readline())

for _ in range(T):
    M=int(sys.stdin.readline())
    print(math.ceil(M/2))
    content=[]

    if M%10==0:
        for _ in range(M//10):
            content.extend(list(map(int,sys.stdin.readline().split())))
    else:
        for _ in range(M//10+1):
            content.extend(list(map(int,sys.stdin.readline().split())))

    solve(content)