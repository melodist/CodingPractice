/**
 * https://leetcode.com/problems/jump-game/
 * Implementation Problem
 */
//1. My Solution
class Solution {
    public boolean canJump(int[] nums) {
        int cur = 0;
        for (int i=0; i<nums.length; i++) {
            if (cur < i) {
                return false;    
            } else {
                cur = Math.max(cur, nums[i]+i);
            }
        }
        return true;
    }
}
