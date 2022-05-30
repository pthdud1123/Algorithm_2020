import sys
#재귀문제 풀 때 꼭 해주어야 함
sys.setrecursionlimit(10**9)

N=int(sys.stdin.readline())

tree=[[]for _ in range(N+1)]
parent=[0 for _ in range(N+1)]

def dfs(start,tree,parents):
    for i in tree[start]:
        if parents[i] ==0:
            parent[i]=start
            dfs(i,tree,parents)

for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1,tree,parent)


for i in range(2,N+1):
    print(parent[i])