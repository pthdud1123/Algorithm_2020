import sys
while(1):
    sentence=list(sys.stdin.readline())
    sentence.pop(-1)
    if sentence[0]=='.'and len(sentence)==1:
        break

    stack=[]
    check=True

    for i in range(len(sentence)):
        if sentence[i].isalpha() or sentence[i] in [' ','.']:
            continue
        elif sentence[i] in ['(','[']:
            stack.append(sentence[i])
        else:
            if sentence[i]==')':
                if stack and stack[-1]=='(':
                    stack.pop(-1)
                else:
                    check=False
                    break
            elif sentence[i]==']':
                if stack and stack[-1]=='[':
                    stack.pop(-1)
                else:
                    check=False
                    break
            else:
                check=False
                break

    if check and not stack :
        print("yes")
    else:
        print("no")