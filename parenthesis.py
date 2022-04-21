import sys
n=int(sys.stdin.readline())

for i in range(n):
    parenthesis = sys.stdin.readline()
    p_list=list(parenthesis)
    sum=0
    for i in p_list:
        if i == '(':
            sum+=1
        elif i == ')':
            sum-=1
        if sum < 0:
            break
    if sum ==0:
        print('YES')
    elif sum != 0:
        print('NO')

