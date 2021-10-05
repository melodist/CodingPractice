/**
 * https://leetcode.com/problems/climbing-stairs/
 * Using Dynamic Programming
 */
//1. My Solution
class Solution {
    public int climbStairs(int n) {
        if (n==1) return 1;
        if (n==2) return 2;
        
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        
        for(int i=3; i<=n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        
        return dp[n];
    }
}

//2. Other Solution
class Solution {
    public int climbStairs(int n) {
        int res=0;
        if(n==0 || n==1) return 1;
        int a=1,b=1;
        for(int i=2;i<=n;i++){
            res=a+b;
            a=b;
            b=res;
        }
        return res;
    }
}
