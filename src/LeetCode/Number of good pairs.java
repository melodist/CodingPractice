/*
https://leetcode.com/problems/number-of-good-pairs/
Using HashMap
*/
class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) { // enhanced for loop
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        }
        
        int ans = 0;
        Set<Integer> countSet = counter.keySet();
        for (int c : countSet) {
            int v = counter.get(c);
            ans += (v * (v-1)) / 2;
        }
        return ans;
    }
}
