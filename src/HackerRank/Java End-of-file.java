/*
* https://www.hackerrank.com/challenges/java-end-of-file/problem
* Input/Output Problem
*/
//1. My Solution
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = 0;
        while(scan.hasNext()){
            i++;
            System.out.println(i + " " + scan.nextLine());
        }
    }
}
