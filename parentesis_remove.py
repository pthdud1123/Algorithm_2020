import sys
from itertools import combinations
sentence=sys.stdin.readline()
sentence=list(sentence)
sentence.pop(-1)

stack=[]
parentesis=[]
answer=set()

#enumerate()함수: 인덱스와 우너소를 동시에 접근하면서 루프를 돌릴 수 있음.
for i, v in enumerate(sentence):
    if v =='(':
        stack.append(i)
    elif v==')':
        start=stack.pop()
        parentesis.append([start,i])

for i in range(1,len(parentesis)+1):
    for j in combinations(parentesis,i):
        tmp = list(sentence)
        for k in j:
            start,end=k
            tmp[start]=''
            tmp[end]=''
        answer.add(''.join(tmp))

for i in sorted(list(answer)):
    print(i)


