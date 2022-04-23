import sys
n=sys.stdin.readline()
circle=[]
stack=[]
for i in range(n):
    x,r=sys.stdin.readline().split()
    a=int(x)-int(r)
    b=int(x)+int(r)
    circle.append([a,i,0])
    circle.append([b,i,1])
circle.sort()

for i in range(n):
    fir=circle[i][2]
    if fir==0:
        stack.append(circle[i])
    else:
        if stack[-1][2]==0:
            if stack[-1][1]==circle[i][1]:
                stack.pop()
            else:
                print("NO")
                exit(0)
print("YES")