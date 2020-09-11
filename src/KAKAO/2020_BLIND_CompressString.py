"""
https://programmers.co.kr/learn/courses/30/lessons/60057/
Implementation Problem
"""
#1. My Solution
import math

def solution(s):
    # 자르는 단위는 모든 문자열에 대하여 고정
    # 무조건 앞에서부터 잘라야 한다
    # n을 하나씩 늘려서 테스트? 1 < n < 문자열 길이
    answer = math.inf
    for i in range(len(s)):
        s_test = test(s,i)
        print(s_test)
        score = len(s_test)
        if score < answer:
            answer = score
    return answer

def test(s,i):
    if len(s) <= i:
        return s
    num = 1
    key = s[0:i+1]
    s_temp = s[i+1:]
    # print(key, s_temp[0:i+1])
    while True:
      if s_temp[0:i+1] == key:
        num += 1
        s_temp = s_temp[i+1:]
      else:
        if num == 1:
          return key + test(s_temp, i)
        else:
          return str(num) + key + test(s_temp, i)

#2. Other Solution
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
