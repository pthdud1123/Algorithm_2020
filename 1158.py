import sys
#import numpy as np

#백준에서는 표준라이브러리 아니면 numpy같은거 못쓰는 구나..
# N,K=sys.stdin.readline().split()
# N,K=int(N),int(K)
N, K = map(int,input().split())
list = [i for i in range(1,N+1)]
# list=np.arange(1,N+1)
# list=list.tolist()

index=0
value=[]

for i in range(N):
    index += (K - 1)
    if index >= len(list):
        index = index % len(list)
    value.append(str(list.pop(index)))


print("<",", ".join(i for i in value),">", sep='')
