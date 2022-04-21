n=int(input())
num=[i for i in range(1,n+1)]
stack=[]
count=0
value=[]

for i in range(n):
    progression = int(input())
    if len(num) != 0:
        while progression >= num[0]:
            stack.append(num.pop(0))
            value.append('+')
            if len(num)==0:
                break

    if stack[-1] == progression :
        if progression == stack[-1] and len(stack) != 0:
            stack.pop(-1)
            value.append('-')
            count+=1

    else:
        count=-1
        break

if count == n:
    print('\n'.join(value))
else:
    print('NO')