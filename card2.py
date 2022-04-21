from collections import deque
import sys

n=int(input())
card=[i for i in range(1,n+1)]
card=deque(card)

while(1):
    if len(card)==1 :
        print(card[0])
        break;

    card.popleft()
    card.rotate(-1)
