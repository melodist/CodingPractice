/*
https://leetcode.com/problems/find-common-characters/submissions/
*/
//#1. My Solution (63ms)
class Solution {
    public List<String> commonChars(String[] A) {
        List<String> ans = new ArrayList();
        String a = A[0];
        for (int i=0; i<a.length(); i++) {
            char c = a.charAt(i);
            boolean flag = true;
            for (int j=1; j<A.length; j++) {
                if (A[j].indexOf(c) == -1) {
                    flag = false;    
                    break;
                }
                else {
                    A[j] = A[j].replaceFirst(Character.toString(c), "");
                }
            }
            if (flag) {
                ans.add(Character.toString(c));                
            }
            
        }
        return ans;
    }
}

//#2. Other Solution (1ms)
class Solution {
    public List<String> commonChars(String[] A) {
        int[] last = count(A[0]);
        for (int i = 1; i < A.length; i++) {
            last = intersection(last, count(A[i])); // find intersection of all strings in A
        }
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (last[i] != 0) {
                char a = 'a';
                a += i;
                String s = String.valueOf(a);
                while (last[i] > 0) {
                    arr.add(s);
                    last[i]--;
                }
            }
        }
        return arr;
    }
    
    // find intersection between frequency array a and b
    int[] intersection(int[] a, int[] b) {
        int[] t = new int[26];
        for (int i = 0; i < 26; i++) {
            t[i] = Math.min(a[i], b[i]);
        }
        return t;
    }
    
    // count frequency of char in string
    int[] count(String str) {
        int[] t = new int[26];
        for (char c : str.toCharArray()) t[c - 'a']++;
        return t;
    }
}
