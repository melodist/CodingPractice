/**
* https://leetcode.com/problems/search-insert-position/
* Using Binary Search
*/
//1. My Solution (0ms)
import java.util.Arrays;


class Solution {
    public int searchInsert(int[] nums, int target) {
        int ans = Arrays.binarySearch(nums, target);
        if (ans < 0) {
            return -ans - 1;
        } else {
            return ans;    
        }
        
    }
}
