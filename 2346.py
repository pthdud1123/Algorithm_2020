import sys
from collections import deque

n=int(sys.stdin.readline())
ballons=list(sys.stdin.readline().split())
ballons=deque(ballons)
index=[i for i in range(1,n+1)]
index=deque(index)
move=0
value=[]

for i in range(len(index)):
    value.append(index.popleft())
    move=int(ballons.popleft())
    if move > 0:
        index.rotate(-(move-1))
        ballons.rotate(-(move-1))
    elif move < 0:
        index.rotate(-move)
        ballons.rotate(-move)

print(" ".join(map(str,value)))