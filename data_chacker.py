import sys
N=int(sys.stdin.readline())
list=[]
c=True

for i in range(N):
    x,r=sys.stdin.readline().split()
    x=int(x)
    r=int(r)
    temp=[]
    temp.append(x-r)
    temp.append(x+r)
    list.append(temp)

list.sort()
stack=[]



def check (left,right):
    for i in range(len(stack)):
        if stack[i][1]<left:
            continue
        elif stack[i][1]>left and stack[i][1]>right:
            continue
        elif (stack[i][1]==left)or(stack[i][1]==right):
            return False
        elif (stack[i][1]>left) and (stack[i][1]<right):
            return False
    return True

for i in range (len(list)): # i는 비교할 대상
    if not stack:
        stack.append(list[i])
    else:
        while stack:
            if list[i][0]>stack[-1][1]:
                stack.pop(-1)
            else:
                break
        if stack and stack[-1][0]<list[i][0] and stack[-1][1]>list[i][1]:
            stack.append(list[i])
        elif not stack:
            stack.append(list[i])
        else:
            c = check(list[i][0],list[i][1])
            stack.append(list[i])
    if c == False:
        break


if c:
    print("YES")
else:
    print("NO")






