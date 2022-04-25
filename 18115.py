import sys
from collections import deque

T=int(sys.stdin.readline())
skill=deque(map(int,sys.stdin.readline().split()))
skill.reverse()
result=deque()
index=1

for i in skill:
    if i ==1:
        result.appendleft(index)
    elif i ==2:
        temp=result.popleft()
        result.appendleft(index)
        result.appendleft(temp)
    else:
        result.append(index)

    index+=1

print(*result)
