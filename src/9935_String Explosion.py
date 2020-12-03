"""
https://www.acmicpc.net/problem/9935
Using stack
1. append character in stack
2. If stack[-1] == bomb[-1], reverse the stack and find the bomb
3. If bomb exists, delete the bomb
"""
#1. My Solution (932ms)
import sys


input = sys.stdin.readline
s = input().strip()
bomb = input().strip()
answer = [' '] * len(s)

idx = 0
for c in s:
    answer[idx] = c
    idx += 1

    if answer[idx - 1] == bomb[-1]:
        if idx - len(bomb) < 0:
            continue

        detected = True;
        for j in range(len(bomb)):
            if answer[idx - j - 1] != bomb[len(bomb) - j - 1]:
                detected = False
                break;
    
        if detected:
            idx -= len(bomb);

print("FRULA") if not idx else print(''.join(answer[:idx]))

#2. Other Solution (240ms)
def main():
    string = input().strip()
    bomb = input().strip()
    bombl = list(bomb)
    b_last = bomb[-1]
    bl = len(bomb)

    ans = []
    for l in string:
        ans.append(l)
        if b_last == l and bombl == ans[-bl:]:
            del ans[-bl:]

    print(''.join(ans) if ans else "FRULA")


if __name__ == '__main__':
    main()
