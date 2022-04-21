import sys
fife=sys.stdin.readline()
fife=list(fife)
stack=[]
value=0

for i in range(len(fife)):
    if fife[i]=='(':
        if fife[i+1] == ')':
            value+=len(stack)
        else:
            stack.append(fife[i])
    elif fife[i]==')':
        if fife[i-1]=='(':
            continue
        else:
            value+=1
            stack.pop()
print(value)