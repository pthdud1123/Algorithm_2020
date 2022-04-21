import sys
from collections import deque

n=sys.stdin.readline()
n=int(n)

q=deque([])

def push(x):
    q.append(x)

def pop():
    if len(q)!=0 :
        print(q[0])
        q.popleft()
    else:
        print(-1)
def size():
    print(len(q))
def empty():
    print(0if len(q) else 1)
def front():
    print(q[0]if len(q) else -1)
def back():
    print(q[-1] if len(q) else -1)

for i in range(n):
    order_split=sys.stdin.readline().split()
    if order_split[0]=='push':
        push(order_split[1])
    elif order_split[0]=='pop':
        pop()
    elif order_split[0]=='size':
        size()
    elif order_split[0]=='empty':
        empty()
    elif order_split[0]=='front':
        front()
    elif order_split[0]=='back':
        back()

