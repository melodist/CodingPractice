def hanoi(n, desks):
    """
    desks[0] : start / desks[1] : temp / desks[2] : end
    hanoi[n-1]
    1 3
    hanoi[n-1]
    """
    start, temp, end = desks
    if n == 1:
        print(f'{start} {end}')
        return

    hanoi(n-1, [start, end, temp])
    print(f'{start} {end}')
    hanoi(n-1, [temp, start, end])

n = int(input())
print(f'{2**n - 1}')
hanoi(n, [1, 2, 3])

