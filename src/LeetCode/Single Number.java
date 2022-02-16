/**
 * https://leetcode.com/problems/single-number/
 * Using bit mask
 */
//1. Simple Solution (1ms)
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int n : nums) {
            ans ^= n;
        }
        return ans;
    }
}

//2. Solution using stream (5ms)
class Solution {
    public int singleNumber(int[] nums) {
        return Arrays.stream(nums).reduce(0, (a, b) -> a ^ b);
    }
}
