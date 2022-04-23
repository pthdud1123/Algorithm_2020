import sys
n=int(sys.stdin.readline())
count=0
for i in range(n):
    goodword=list(sys.stdin.readline())
    goodword.pop(-1)
    stack=[]
    for i,w in enumerate(goodword):
        if not stack:
            stack.append(w)
        else:
            if w == stack[-1]:
                stack.pop()
            else:
                stack.append(w)
    if not stack:
        count+=1
print(count)
