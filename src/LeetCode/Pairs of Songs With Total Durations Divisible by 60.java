/*
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
Using HashMap
*/
//Solution using HashMap (9ms)
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int ans = 0;
        Map<Integer, Integer> mods = new HashMap<Integer, Integer>();
        for (int i=0; i<time.length; i++) {
            int mod = time[i] % 60;
            mods.put(mod, mods.getOrDefault(mod, 0)+1);
        }
        
        for (int i=1; i<30; i++) {
            int a = mods.getOrDefault(i, 0);
            int b = mods.getOrDefault(60-i, 0);
            ans += a * b;
        }
        int c = mods.getOrDefault(0, 0);
        int d = mods.getOrDefault(30, 0);
        
        return ans + c * (c-1) / 2 + d * (d-1) / 2;
    }
}

//Solution using Array (2ms)
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int ans = 0;
        int[] mods = new int[60];
        for (int i=0; i<time.length; i++) {
            int mod = time[i] % 60;
            ans += mods[(60 - mod) % 60];
            mods[mod]++;
        }
        
        return ans;
    }
}
