import sys
N=int(sys.stdin.readline())

top=list(map(int,sys.stdin.readline().split()))
cnt=[0]*(N+1)
near=[[int(1e9),int(1e9)]for _ in range(N+1)]
stack=[]


#왼쪽에 있는 건물 부터 체크
for i,v in enumerate(top):
    while stack and stack[-1][1]<=v:
        stack.pop()
    cnt[i+1]=len(stack)

    if stack:
        d=abs(stack[-1][0]-(i+1))
        if d<near[i+1][1]:
            near[i+1][0]=stack[-1][0]
            near[i+1][1]=d
        elif d==near[i+1][1] and stack[-1][0]<near[i+1][0]:
            near[i+1][0]=stack[-1][0]

    stack.append([i+1,v])

stack.clear()
for i,v in reversed(list(enumerate(top))):
    while stack and stack[-1][1] <= v:
        stack.pop()
    cnt[i + 1] += len(stack)

    if stack:
        d = abs(stack[-1][0] - (i + 1))
        if d < near[i + 1][1]:
            near[i + 1][0] = stack[-1][0]
            near[i + 1][1] = d
        elif d == near[i + 1][1] and stack[-1][0] < near[i + 1][0]:
            near[i + 1][0] = stack[-1][0]

    stack.append([i + 1, v])

for i in range(1,N+1):
    if cnt[i]==0:
        print(0)
    else:
        print(str(cnt[i]),str(near[i][0]))

