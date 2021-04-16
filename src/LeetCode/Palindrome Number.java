/*
https://leetcode.com/problems/palindrome-number/
Implementation Problem
*/
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int a = x;
        int temp = 0;
        while (a > 0) {
            temp *= 10;
            temp += a % 10;
            a /= 10;
        }
        if (x == temp) {
            return true;
        }
        else {
            return false;
        }
    }
}
