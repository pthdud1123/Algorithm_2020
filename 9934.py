import sys
sys.setrecursionlimit(10**6)


K=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
value=[[] for _ in range(K+1)]

def treemake(arr,level):
    length=len(arr)
    mid=length//2

    if len(arr)==1:
        value[level].append(arr[mid])
        return

    value[level].append(arr[mid])
    treemake(arr[:mid],level+1)
    treemake(arr[mid:],level+1)

treemake(arr, 0)

for i in range(K):
    for j, data in enumerate(value[i]):
        print(data, end=" ")
    print()

