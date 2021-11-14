/**
 * https://leetcode.com/problems/pascals-triangle-ii/
 * Using Dynamic Programming
 */
//1. My Solution (3ms)
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> answer = new ArrayList<>();
        answer.add(1);
        List<Integer> prev = new ArrayList<>(answer);
        
        for (int i=1; i<=rowIndex; i++) {
            answer.add(0);
            prev.add(0);
            
            for (int j=1; j<=i; j++) {
                answer.set(j, prev.get(j) + prev.get(j-1));
            }
            
            prev = new ArrayList<>(answer);
        }
        return answer;
    }
}

//2. Other Solution
class Solution {
    public List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> result = new ArrayList<>(rowIndex + 1);
        for (int i = 0; i < rowIndex + 1; i++) {
            result.add(1);
            for (int j = i - 1; j > 0; j--) {
                result.set(j, result.get(j) + result.get(j - 1));
            }
        }

        return result;
    }
}
