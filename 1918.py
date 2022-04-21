import sys
n=int(sys.stdin.readline())
posterior=sys.stdin.readline()
posterior=list(posterior)
posterior.pop(-1)
num=[]
stack=[]
operator=['*','/','+','-']

for i in range(n):
    a=int(sys.stdin.readline())
    num.append(a)

for i,w in enumerate(posterior):
    if w in operator and stack:
        num1=stack.pop(-1)
        num2=stack.pop(-1)
        if w =='*':
            stack.append(num2*num1)
        elif w=='/':
            stack.append(num2/num1)
        elif w=='+':
            stack.append(num2+num1)
        elif w=='-':
            stack.append(num2-num1)
    else:
        stack.append(num[ord(w)-ord('A')])


number=stack.pop()
print(format(number,".2f"))