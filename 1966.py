from collections import deque
import sys

T=int(sys.stdin.readline())

for t in range(T):
    N, D = sys.stdin.readline().split()
    N = int(N)
    D = int(D)
    important_t = list(sys.stdin.readline().split())
    max_important=important_t.copy()
    max_important.sort(reverse=True) #중요도를 내림차순으로 나타내는 것
    important=deque(important_t) # 문서 중요도 순위 큐로 표현
    index=[i for i in range(0,N)]
    index=deque(index)
    value=0 #몇번째 문서가 출력되고 있는지 나타냄

    while(1):
        if max_important[0] == important[0]:
            max_important.pop(0)
            important.popleft()
            if index[0]==value:
                print(value+1)
                break
            else:
                value+=1
                index.popleft()
        else:
            while max_important[0] != important[0]:
                important.rotate(-1)
                index.rotate(-1)






