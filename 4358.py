# import sys
# from collections import defaultdict
# tree=defaultdict(int)
# all=0
# while(1):
#     name=sys.stdin.readline()
#     if name =='\n':
#         break
#     name=name.rstrip()
#     tree[name]+=1
#     all+=1
#
# trees=list(tree.keys())
# trees.sort()
# for i in trees:
#     print(i,round(tree[i]*100/all,4))
#

import sys
import math
tree={}
sum=0
input=sys.stdin.readline
while(1):
    name=input().rstrip()
    if not name:
        break
    if name in tree:
        tree[name] += 1
    else:
        tree[name] = 1
    sum+=1



# trees=list(tree.keys())
# trees.sort()
trees=sorted(tree.keys())
for i in trees:
    #print(i,round(tree[i]*100/sum,4)) <--틀렸던 이유....
    print('%s %.4f' %(i,tree[i]/sum*100))



