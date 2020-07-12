"""
https://www.hackerrank.com/challenges/merging-communities/problem
Using Disjoint sets
"""
N, Q = map(int, input().split())

# dict_one : root of each nodes
# dict_two : leaves of nodes which is root

dict_one = dict()
dict_two = dict()

for i in range(N):
    dict_one[i] = str(i)
    dict_two[str(i)] = [i]

for q in range(Q):
    command = input().split()
    if command[0] == 'Q':
        I = int(command[1]) - 1
        community = dict_one[I]
        print(len(dict_two[community]))
    else:
        I, J = int(command[1]) - 1, int(command[2]) - 1
        com1, com2 = dict_one[I], dict_one[J]
        if com1 != com2:
            x, y = dict_two[com1], dict_two[com2]
            if len(x) > len(y):
                x, y = y, x
                com1, com2 = com2, com1
            for k in x:
                dict_one[k] = com2
            y.extend(x)
            del dict_two[com1]

    print(dict_one, dict_two)
