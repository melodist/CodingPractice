"""
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
Using Hashmap
"""
dic = {}
for num in A:
    dic[num] = 0
i = 1
while True:
    if i not in dic.keys():
        print(i)
        break
