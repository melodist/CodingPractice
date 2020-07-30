"""
https://programmers.co.kr/learn/courses/30/lessons/42746/
"""
#1. My Solution
def solution(numbers):
    def compare(a, b):
        # "12" + "121" > "121" + "12"
        if int(arr[a] + arr[b]) > int(arr[b] + arr[a]):
            return True

    def divide(left, right):
        if left >= right: return
        mid = (left + right) // 2
        divide(left, mid)
        divide(mid+1, right)

        l = left
        r = mid+1
        temp = []
        while l < mid+1 and r < right+1:
            if compare(l, r):
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[r])
                r += 1

        if l == mid + 1:
            temp += arr[r:right+1]
        else:
            temp += arr[l:mid+1]

        arr[left:right+1] = temp

    arr = [str(i) for i in numbers]

    divide(0, len(numbers)-1)
    return ''.join(arr) if arr[0] != '0' else '0'

#2. Other Solution
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # x <= 1000이기 때문에 x*3으로 정렬 가능
    return str(int(''.join(numbers)))
