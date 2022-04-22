import sys

N=sys.stdin.readline()
H=list(map(int,sys.stdin.readline().split()))


value=[]
stack=[] #높이가 저장되어 있는 인덱스번호 저장

for i,w in enumerate(H):
    if not stack:
        value.append(0)
        stack.append(i)
    else:
        if H[stack[-1]] > w:
            value.append(stack[-1]+1)
            stack.append(i)
        elif H[stack[-1]] < w:
            while stack:
                if not stack:
                    value.append(0)
                    stack.append(i)
                    break
                elif H[stack[-1]] < w:
                    stack.pop(-1)
                    if not stack:
                        value.append(0)
                        stack.append(i)
                        break
                elif H[stack[-1]] > w:
                    value.append(stack[-1]+1)
                    stack.append(i)
                    break

print(' '.join(map(str,value)))