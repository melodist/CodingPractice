/*
* https://programmers.co.kr/learn/courses/30/lessons/12911?language=java
* Using bit counting
*/
// 1. My Solution
class Solution {
    public int solution(int n) {
        int answer = n+1;
        int n_bit = Integer.bitCount(n);
        while (true) {
            if (Integer.bitCount(answer) == n_bit) {
                return answer;
            }
            answer++;
        }
    }
}
