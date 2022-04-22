import sys

parenthesis=sys.stdin.readline()
parenthesis=list(parenthesis)
stack=[]
check=True

for i, w in enumerate(parenthesis):
    if w == '(' or w=='[':
        stack.append(w)
    elif w ==')':
        if stack[-1] == '[' or not stack:
            check=False
            break
        elif stack[-1] =='(':
            stack.pop(-1)
            stack.append(2)
        else:
            value=0
            while stack[-1] !='(':
                if stack[-1] =='[' or not stack or stack[-1]==')':
                    check = False
                    break
                value+=int(stack.pop(-1))
            stack.pop(-1) #'(' pop해주기
            stack.append(value*2)
    elif w==']':
        if stack[-1] == '(' or not stack:
            check = False
            break
        elif stack[-1] == '[':
            stack.pop(-1)
            stack.append(3)
        else:
            value=0
            while stack[-1]!='[':
                if stack[-1] == '(' or not stack or stack[-1]==']':
                    check = False
                    break
                value+=int(stack.pop(-1))
            stack.pop(-1)
            stack.append(value*3)

if check:
    for i in ['(','[']:
        if i in stack:
            print(0)
            exit()
    print(sum(stack))
    # else:
    #     print(sum(stack))
elif not stack or check==False:
    print(0)


