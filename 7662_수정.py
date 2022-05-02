import sys
from collections import deque

T=int(sys.stdin.readline())

for t in range(T):
    K=int(sys.stdin.readline())
    q=deque()
    max=-1e10
    min=1e10
    list = []
    for k in range(K):
        o,n=sys.stdin.readline().split()
        n=int(n)

        if o == 'I':
            q.append(n)
            list.append(n)

        if q:
            list.sort()
            max=list[-1]
            min=list[0]

        if o == 'D':
            if n == 1: #최대값 삭제
                while q and q[0]!=max:
                    q.rotate(-1)
                if q and q[0]==max:
                    q.popleft()
                    list.pop(-1)
                if q:
                    max=list[-1]
                else:
                    max=-1e10
            elif n==-1:
                while q and q[0]!=min:
                    q.rotate(-1)
                if q and q[0]==min:
                    q.popleft()
                    list.pop(0)
                if q:
                    min=list[0]
                else:
                    min=1e10

    if q:
        print(max, min)
    else:
        print("EMPTY")

