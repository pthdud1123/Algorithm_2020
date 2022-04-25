import sys
N=int(sys.stdin.readline())
stack=[]
count=0
for n in range(N):
    x,y = map(int,sys.stdin.readline().split())
    if y==0:
        count+=len(stack)
        stack.clear()
    elif not stack:
        stack.append(y)
    else:
        if stack[-1]<y:
            stack.append(y)
        elif stack[-1]>y:
            while stack and stack[-1] > y:
                stack.pop()
                count+=1
            if stack and stack[-1] == y:
                continue
            stack.append(y)


print(count+len(stack))
