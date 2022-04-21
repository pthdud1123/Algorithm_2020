import sys
notation=sys.stdin.readline()
notation=list(notation)
notation.pop(-1)
operator=['(',')','*','/','+','-']
value=''
stack=[]
for i,w in enumerate(notation):
    if w in operator:
        if w =='(':
            stack.append(w)
        elif w=='*' or w == '/':
            while stack and (stack[-1] =='*' or stack[-1]=='/'):
                value+=stack.pop(-1)
            stack.append(w)
        elif w=='+' or w=='-':
            while stack and stack[-1] != '(':
                value+=stack.pop(-1)
            stack.append(w)
        elif w==')':
            while stack and stack[-1] !='(':
                value+=stack.pop(-1)
            stack.pop()
    else:
        value+=w

while stack:
    value+=stack.pop()

print(value)


