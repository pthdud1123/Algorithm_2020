import sys
from collections import deque
T=int(sys.stdin.readline()) #테스트 케이스 개수


for t in range(T):
    check=True
    reverse=0#홀수 일 때 역방향
    p = list(sys.stdin.readline())  # 실행할 함수의 명령
    n = int(sys.stdin.readline())  # 배열의 크기
    inputlist = deque(sys.stdin.readline().rstrip()[1:-1].split(","))  # 배열 값

    if n==0:
        inputlist=deque

    for i,w in enumerate(p):
        if w=='D':
            if not inputlist:
                check=False
                break
            else:
                if reverse%2 == 0:
                    inputlist.popleft()
                else:
                    inputlist.pop()
        elif w =='R':
            reverse+=1

    if check:
        if reverse % 2 == 1:
            inputlist.reverse()
        print('['+','.join(inputlist)+']')
    else:
        print("error")

