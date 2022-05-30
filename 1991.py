import sys
#A:65, .:46
N=int(sys.stdin.readline())
tree=[[]for _ in range(26+1)]
pre_check=[True for _ in range(26+1)]
ino_check=[True for _ in range(26+1)]
pos_check=[True for _ in range(26+1)]
pre=[]
ino=[]
pos=[]

#전위 순회 : preorder traversal, 중위 순회 : Inorder traversal, 후위 순회 : postorder traversal

def preorder(index):
    if pre_check[index]:
        pre.append(chr(65+index))
        pre_check[index]=False
    if tree[index][0] != -19:
        preorder(tree[index][0])
    if tree[index][1] != -19:
        preorder(tree[index][1])

def inorder(index):
    if tree[index][0] != -19:
        inorder(tree[index][0])
    if ino_check[index]:
        ino.append(chr(65 + index))
        ino_check[index]=False
    if tree[index][1] != -19:
        inorder(tree[index][1])

def postorder(index):
    if tree[index][0] != -19:
        postorder(tree[index][0])
    if tree[index][1] != -19:
        postorder(tree[index][1])
    if pos_check[index]:
        pos.append(chr(65 + index))
        pos_check[index]=False

for _ in range(N):
    root,l,r=sys.stdin.readline().split()
    tree[ord(root)-65].append(ord(l)-65)
    tree[ord(root)-65].append(ord(r)-65)

preorder(0)
inorder(0)
postorder(0)

for i in range(len(pre)):
    print(pre[i],end="")
print()
for i in range(len(ino)):
    print(ino[i],end="")
print()
for i in range(len(pos)):
    print(pos[i],end="")
