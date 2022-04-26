import sys
N,M=map(int,sys.stdin.readline().split())
list=[]
for i in range(N):
    setence=sys.stdin.readline().rstrip()
    list.append(setence)

s=set(list)
count=0

for i in range(M):
    q=sys.stdin.readline().rstrip()
    temp=[q]
    temp=set(temp)
    if s&temp:
        count+=1

print(count)