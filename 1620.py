import sys
N,M=map(int,sys.stdin.readline().split())

dict={}

for i in range(N):
    name=sys.stdin.readline().rstrip()
    dict[i+1]=name
    dict[name]=i+1

for i in range(M):
    quest=sys.stdin.readline().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])





