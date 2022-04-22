import sys

parenthesis=sys.stdin.readline()
parenthesis=list(parenthesis)
stack=[]
check=True

for i, w in enumerate(parenthesis):
    if w =='(' or w == '[':
        stack.append(w)
    elif w ==')':
        value=0
        while stack:
            if not stack or stack[-1]=='[' or stack[-1]==']' or stack[-1]==')':
                check=False
                break
            elif stack[-1]=='(':
                stack.pop(-1)
                if value == 0:
                    value = 1
                stack.append(value * 2)
                break
            else:
                value+=int(stack.pop(-1))
        if not stack:
            check=False
            break

    elif w==']':
        value=0
        while stack:
            if not stack or stack[-1]=='('or stack[-1]==')'or stack[-1]==']':
                check=False
                break
            elif stack[-1]=='[':
                stack.pop(-1)
                if value == 0:
                    value = 1
                stack.append(value * 3)
                break
            else:
                value+=int(stack.pop(-1))
        if not stack:
            check=False
            break


if check:
    for i in ['(', '[',']',')']:
        if i in stack:
            print(0)
            exit()
    print(sum(stack))
elif not stack or check == False:
    print(0)
