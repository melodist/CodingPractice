"""
https://programmers.co.kr/learn/courses/30/lessons/67256
Implementation Problem
"""
def solution(numbers, hand):
    def near_left(n):
        dist_l_y, dist_l_x = divmod(abs(n - thumb_l), 3)
        dist_r_y, dist_r_x = divmod(abs(n - thumb_r), 3)

        if dist_l_x + dist_l_y < dist_r_x + dist_r_y:
            return True
        elif dist_l_x + dist_l_y == dist_r_x + dist_r_y:
            return True if hand == 'left' else False
        else:
            return False
        
    nums = {1:'L', 4:'L', 7:'L', 3:'R', 6:'R', 9:'R'}
    answer = ''
    thumb_l = 10
    thumb_r = 12
    
    for n in numbers:
        if n == 0:
            n = 11
        if n in nums:
            answer += nums[n]
            if nums[n] == 'L':
                thumb_l = n
            else:
                thumb_r = n
        else:
            if near_left(n):
                answer += 'L'
                thumb_l = n
            else:
                answer += 'R'
                thumb_r = n
                
    return answer
