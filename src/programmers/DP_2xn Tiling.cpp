"""
https://programmers.co.kr/learn/courses/30/lessons/12900?language=cpp#
Using dynamic programming
"""
#1. My Solution
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    vector <int> dp(n+1);
    int MOD = 1000000007;
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i < dp.size(); i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % MOD;
    }
    
    return dp[n];
}
