"""
https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
"""
def decodeHuff(root, s):
    #Enter Your Code Here
    cur = root
    i = 0
    ans = ""
    while i < len(s):
        while cur.data == '\0':
            cur = cur.left if s[i] == '0' else cur.right         
            i += 1
        ans += cur.data
        cur = root
    
    print(ans)
