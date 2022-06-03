import sys
sys.setrecursionlimit(10**6)

list=[]

while True:
    try:
        num=int(sys.stdin.readline())
        list.append(num)
    except:
        break

def maketree(first,end): #key: 부모의 key값, list index
    if first > end:
        return
    mid=end+1
    for i in range(first+1,end+1):
        if list[first]<list[i]:
            mid=i
            break
    maketree(first+1,mid-1)
    maketree(mid,end)
    print(list[first])

maketree(0,len(list)-1)