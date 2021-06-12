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

#2. Other Solution (64ms)
import sys
def solution():
    T = int(sys.stdin.readline())
    ips = [sys.stdin.readline().rstrip().split('.') for i in range(T)]
    net_addr = []
    net_mask = []
    for i in range(4):
        min_ip = int(ips[0][i])
        max_ip = int(ips[0][i])
        for tmp_ip in ips:
            if max_ip < int(tmp_ip[i]):
                max_ip = int(tmp_ip[i])
            if min_ip > int(tmp_ip[i]):
                min_ip = int(tmp_ip[i])
        if 255 == 256 + (~max_ip^min_ip):
            net_mask.append(255)
        else:
            for j in range(9):
                if -(~max_ip^min_ip) <= 1<<j:
                    net_mask.append(256 - (1<<j))
                    for k in range(3):
                        net_mask.append(0)
                    break
        net_addr.append(int(ips[0][i])&net_mask[i])
    print("{}.{}.{}.{}".format(net_addr[0], net_addr[1], net_addr[2], net_addr[3]))
    print("{}.{}.{}.{}".format(net_mask[0], net_mask[1], net_mask[2], net_mask[3]))

solution()
