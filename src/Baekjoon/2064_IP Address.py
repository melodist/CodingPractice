"""
https://www.acmicpc.net/problem/2064
Implementation Problem
Find minimum index of 1 and makes all digits 0 after the index
"""
#1. My Solution (160ms)
from functools import reduce


n = int(input())
ips = []
ip1 = [[*'0' * (10 - len(bin(a))) + bin(a)[2:]] for a in [*map(int, (input().split('.')))]]
diffs = 0

for _ in range(n-1):
	ip2 = [[*'0' * (10 - len(bin(a))) + bin(a)[2:]] for a in [*map(int, (input().split('.')))]]
	for i in range(4):
	    for j in range(8):
		    if ip1[i][j] != ip2[i][j]:
		        ip1[i][j] = 'e'
		        diffs += 1

ip_concat = reduce(lambda x, y: x + y, [''.join(r) for r in ip1])

# Find minimum index of 1
m = ip_concat.index('e') if diffs > 0 else 32

network_ip = [*ip_concat]
for i in range(m, 32):
    network_ip[i] = '0'
network_ip = ''.join(network_ip)
network_ip = [int(network_ip[i*8:(i+1)*8], 2) for i in range(4)]
print('.'.join(map(str, network_ip)))

mask = bin(2**32 - 2**(32-m))[2:]
mask_concat = '0' * (32 - len(mask)) + mask
masks = [int(mask_concat[i*8:(i+1)*8], 2) for i in range(4)]
print('.'.join(map(str, masks)))
