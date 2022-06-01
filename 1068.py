import sys

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
eraser=int(sys.stdin.readline())

def noderemove(eraser):
    arr[eraser]=-2
    for i in range(len(arr)):
        if arr[i]==eraser:
            noderemove(i)

count=0
minus=0
if arr[eraser] ==-1:
    print(0)
else:
    noderemove(eraser)
    for i in range(len(arr)):
        if arr[i] !=-2 and i not in arr:
            count+=1
    print(count)

