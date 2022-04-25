import sys
T=int(sys.stdin.readline())
for t in range(T):
    pw=list(sys.stdin.readline().rstrip())
    left,right=[],[]
    for i,w in enumerate(pw):
        if w=='<':
            if left:
                right.append(left.pop(-1))
        elif w=='>':
            if right:
                left.append(right.pop(-1))
        elif w=='-':
            if left:
                left.pop(-1)
        else:
            left.append(w)
    print(''.join(left)+''.join(reversed(right)))

