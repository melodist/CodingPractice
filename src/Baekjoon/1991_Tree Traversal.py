"""
https://www.acmicpc.net/problem/1991
"""
#1. Non-recursive Solution
from collections import deque


n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = {}
    if left != '.':
        tree[root]['L'] = left
    if right != '.':
        tree[root]['R'] = right

# preorder
q = deque(['A'])
ans = ''
visited = set()
while q:
    cur = q.popleft()
    ans += cur
    temps = []
    if 'L' in tree[cur]:
        temps.append(tree[cur]['L'])

    if 'R' in tree[cur]:
        temps.append(tree[cur]['R'])
        
    q = deque(temps) + q

print(ans)

# inorder
st = ['A']
ans = ''
visited = set()
while st:
    cur = st[-1]
    temp = cur
    while 'L' in tree[temp]:
        nt = tree[temp]['L']
        if nt not in visited:
            st.append(nt)
            temp = nt
            visited.add(nt)
        else:
            break

    ans += st.pop()
    
    if 'R' in tree[temp] and tree[temp]['R'] not in visited:
        st.append(tree[temp]['R'])
        visited.add(tree[temp]['R'])
        
print(ans)
    
# postorder
st = ['A']
ans = ''
visited = set()
while st:
    cur = st[-1]
    temp = cur
    temps = []
    while 'L' in tree[temp]:
        nt = tree[temp]['L']
        if nt not in visited:
            temps.append(nt)
            temp = nt
            visited.add(nt)
        else:
            break

    if 'R' in tree[temp] and tree[temp]['R'] not in visited:
        temps.append(tree[temp]['R'])
        visited.add(tree[temp]['R'])
        
    if not temps:
        ans += st.pop()
        
    st += temps
    
print(ans)

#2. Recursive Solution
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = {}
    tree[root]['L'] = left
    tree[root]['R'] = right

# preorder
def preorder(node):
    if node == '.':
        return ''
    
    return node + preorder(tree[node]['L']) + preorder( tree[node]['R'])

print(preorder('A'))

# inorder
def inorder(node):
    if node == '.':
        return ''
    
    return inorder(tree[node]['L']) + node + inorder(tree[node]['R'])

print(inorder('A'))
    
# postorder
def postorder(node):
    if node == '.':
        return ''
    
    return postorder(tree[node]['L']) + postorder(tree[node]['R']) + node

print(postorder('A'))
