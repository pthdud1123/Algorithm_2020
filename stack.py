#input()함수를 사용할 경우, 시간초과 에러가뜨므로 시간 단축을 위해 sys.stdin.readlin()을 사용한다.
#입출력 속도 비교 : sys.stdin.radline> raw_input()>input()
import sys
n=sys.stdin.readline()
n=int(n)

stack=[]

def push(x):
    return stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    print(0 if stack else 1)

def top():
    print(stack[-1] if stack else -1)

for i in range(n):
    input_split = sys.stdin.readline().split()
    order=input_split[0]

    if order =='push':
        push(input_split[1])
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()

