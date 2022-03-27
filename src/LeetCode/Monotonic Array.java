/**
 * https://leetcode.com/problems/monotonic-array/submissions/
 * Using Array
 */
//1. My Solution (2ms, 94MB)
class Solution {
    public boolean isMonotonic(int[] nums) {
        if (nums.length < 3) return true;
        
        int currDiff;
        int prevDiff = nums[1] - nums[0];
        for (int i=2; i<nums.length; i++) {
            currDiff = nums[i] - nums[i-1];
            if (currDiff * prevDiff < 0) return false;
            if (currDiff != 0) prevDiff = currDiff;
        }
        return true;
    }
}

//2. Other Solution (3ms, 52MB)
class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean isIncreasing = true;
        boolean isDecreasing = true;
        for (int i=1; i<nums.length; i++) {
            if (nums[i] - nums[i-1] > 0) isDecreasing = false;
            if (nums[i] - nums[i-1] < 0) isIncreasing = false;
        }
        return isIncreasing || isDecreasing;
    }
}
