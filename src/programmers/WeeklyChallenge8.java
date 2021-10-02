/**
 * https://programmers.co.kr/learn/courses/30/lessons/86491
 * Implementation Problem
 */

//1. My Solution
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;


class Solution {
    public int solution(int[][] sizes) {
        List<Integer> max = Arrays.stream(sizes)
                .map(x -> Arrays.stream(x).max().getAsInt())
                .collect(Collectors.toList());
        int maxValue = max.stream().mapToInt(x -> x).max().getAsInt();
        List<Integer> min = Arrays.stream(sizes)
                .map(x -> Arrays.stream(x).min().getAsInt())
                .collect(Collectors.toList());
        int minValue = min.stream().mapToInt(x -> x).max().getAsInt();
        return maxValue * minValue;
    }
}

//2. Other Solution
import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        return Arrays.stream(sizes).reduce((a, b) -> new int[]{
                Math.max(Math.max(a[0], a[1]), Math.max(b[0], b[1])), Math.max(Math.min(a[0], a[1]), Math.min(b[0], b[1]))
        }).map(it -> it[0] * it[1]).get();
    }
}
