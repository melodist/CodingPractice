/*
https://programmers.co.kr/learn/courses/30/lessons/1845
Using Hash
*/
//1. My Solution
import java.util.Map;
import java.util.HashMap;


class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        int answer = 0;
        Map<Integer, Integer> dict = new HashMap<>();
        for (int a:nums) {
            if (!dict.containsKey(a)) {
                dict.put(a, 0);
                answer += 1;
            }
        }

        if (answer > n / 2) {
            return n / 2;
        }
        return answer;
    }
}

//2. Other Solution
import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {

            HashSet<Integer> hs = new HashSet<>();

            for(int i =0; i<nums.length;i++) {
                hs.add(nums[i]);
            }

            if(hs.size()>nums.length/2)
                return nums.length/2;

            return hs.size();
    }
}
