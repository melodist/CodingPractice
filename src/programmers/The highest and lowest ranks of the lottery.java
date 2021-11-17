/**
 * https://programmers.co.kr/learn/courses/30/lessons/77484?language=java
 * Implementation Problem
 */
//1. My Solution
import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        List<Integer> l = Arrays.stream(lottos)
                            .boxed()
                            .collect(Collectors.toList());
        List<Integer> w = Arrays.stream(win_nums)
                            .boxed()
                            .collect(Collectors.toList());
    
        w.retainAll(l); // make intersection in w

        int intersection = w.size();
        int zeros = Collections.frequency(l, 0);

        answer[0] = 7 - intersection - zeros > 5 ? 6 : 7 - intersection - zeros;
        answer[1] = 7 - intersection > 5 ? 6 : 7 - intersection;
        
        return answer;
    }
}
