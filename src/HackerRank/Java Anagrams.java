/**
* https://www.hackerrank.com/challenges/java-anagrams/problem
*/
// 1. My Problem
static boolean isAnagram(String a, String b) {           
    // test for invalid input   
    if( a == null || b == null || a.equals("") || b.equals("") )
        throw new IllegalArgumentException();

    // initial quick test for non-anagrams
    if ( a.length() != b.length() )
        return false;

    a = a.toLowerCase();
    b = b.toLowerCase();

    int[] ca = new int[26];
    int[] cb = new int[26];

    for (int i = 0; i < a.length(); i++) {
        ca[a.charAt(i) - 97]++;
        cb[b.charAt(i) - 97]++;
    }

    for (int i = 0; i<26; i++) {
        if (ca[i] != cb[i]) {
            return false;
        }
    }

    return true;
}
