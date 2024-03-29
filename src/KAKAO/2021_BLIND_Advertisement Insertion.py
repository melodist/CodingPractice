"""
https://programmers.co.kr/learn/courses/30/lessons/72414?language=python3
Using Prefix Sum
"""
#1. My Solution
def solution(play_time, adv_time, logs):
    def log_to_sec(log):
        hh, mm, ss = map(int, log.split(':'))
        return hh * 3600 + mm * 60 + ss
    
    play_time_sec = log_to_sec(play_time)
    adv_time_sec = log_to_sec(adv_time)
    total_time = [0] * (100 * 60 * 60)
    
    #1. total_time[i]: number of intervals start at i sec
    for l in logs:
        start_time, end_time = l.split('-')
        start_time_sec = log_to_sec(start_time)
        end_time_sec = log_to_sec(end_time)
        
        total_time[start_time_sec] += 1
        total_time[end_time_sec] -= 1
    
    #2. total_time[i]: number of intervals playing at i sec
    for i in range(1, play_time_sec):
        total_time[i] += total_time[i-1]
    
    #3. total_time[i]: number of accumulated sum of time at i sec
    for i in range(1, play_time_sec):
        total_time[i] += total_time[i-1]
    
    #4. Find index i when total_time[i] is maximum, and find the answer
    max_time = 0
    answer_sec = 0
    for i in range(adv_time_sec - 1, play_time_sec):
        if max_time < total_time[i] - total_time[i - adv_time_sec]:
            answer_sec = i - adv_time_sec + 1
            max_time = total_time[i] - total_time[i - adv_time_sec]
                
    return f"{answer_sec//3600:02d}:{answer_sec%3600//60:02d}:{answer_sec%3600%60:02d}"
