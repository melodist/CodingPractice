/**
 * https://www.hackerrank.com/challenges/java-interface/problem
 * Using Interface
 */
//1. My Solution
class MyCalculator implements AdvancedArithmetic {
    public int divisor_sum(int n) {
        int answer = 0;
        for (int i=1; i<=n; i++) {
            if (n % i == 0) {
                answer += i;
            }
        }
        return answer;
    }
}
