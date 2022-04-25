import sys
from collections import deque
import math

N,M=map(int,sys.stdin.readline().split())
list=deque(i for i in range(1,N+1))
poplist=map(int,sys.stdin.readline().split())
count=0


for i,w in enumerate(poplist):
    size=math.ceil(len(list)/2)
    temp_count=0
    for j in range(len(list)):
        if w==list[j]:
            if temp_count>0:
                if temp_count>size:
                    temp_count=len(list)-temp_count
                    list.rotate(temp_count)
                else:
                    if temp_count==size and len(list)%2==1:
                        temp_count = len(list) - temp_count
                        list.rotate(temp_count)
                    else:
                        temp_count=temp_count*-1
                        list.rotate(temp_count)
            list.popleft()
            count+=abs(temp_count)
            break
        else:
            temp_count+=1

print(count)

