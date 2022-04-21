import sys
n=int(input())
deck=[]
def push_front(x):
    deck.insert(0,x)
def push_back(x):
    deck.append(x)
def pop_front():
    if len(deck) ==0:
        print(-1)
    else:
        print(deck.pop(0))
def pop_back():
    if len(deck)==0:
        print(-1)
    else:
        print(deck.pop(-1))
def size():
    print(len(deck))
def empty():
    print(0 if deck else 1)
def front():
    print(deck[0] if deck else -1)
def back():
    print(deck[-1] if deck else -1)

for i in range(n):
    order_split=sys.stdin.readline().split()
    if order_split[0] == 'push_front':
        push_front(order_split[1])
    elif order_split[0] == 'push_back':
        push_back(order_split[1])
    elif order_split[0]=='pop_front':
        pop_front()
    elif order_split[0] == 'pop_back':
        pop_back()
    elif order_split[0] == 'size':
        size()
    elif order_split[0]=='empty':
        empty()
    elif order_split[0] == 'front':
        front()
    elif order_split[0] =='back':
        back()

