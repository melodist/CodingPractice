/*
* https://www.acmicpc.net/problem/1260
* Using DFS and BFS
*/
//1. My Solution (364ms)
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class main{

     public static void main(String []args) throws IOException {
        
        // Input Process
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        
        StringTokenizer stk = new StringTokenizer(s);
        String[] strings = new String[stk.countTokens()];
        int[] cond = new int[stk.countTokens()];
        int i = 0;
        
        while (stk.hasMoreTokens()) {
            strings[i] = stk.nextToken();
            cond[i] = Integer.parseInt(strings[i]);
            i++;
        }
        
        int n = cond[0];
        int m = cond[1];
        int v = cond[2];
        
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (i = 0; i <= n; i++) {
            ArrayList<Integer> adjs = new ArrayList<>();
            adj.add(adjs);
        }
        
        for (int k = 0; k < m; k++) {
            s = bf.readLine();
            stk = new StringTokenizer(s);
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        
        // Problem Process
        // DFS
        for (i = 0; i <= n; i++) {
            adj.get(i).sort(Comparator.reverseOrder());
        }
        
        boolean[] visited = new boolean[n+1];
        Deque<Integer> q = new ArrayDeque<>();
        q.push(v);
        
        while (!q.isEmpty()) {
            int start = q.pop();
            if (visited[start]) {
                continue;
            }
            
            System.out.print(start);
            System.out.print(" ");
            
            ArrayList<Integer> adjs = adj.get(start);
            for(i=0; i<adjs.size(); i++) {
                int next = adjs.get(i);
                if (!visited[next]) {
                    q.push(next);
                }
            }
            visited[start] = true;
        }
        System.out.println();
        
        // BFS
        for (i = 0; i <= n; i++) {
            adj.get(i).sort(null);
        }
        
        visited = new boolean[n+1];
        visited[v] = true;
        q.offer(v);
        
        while (!q.isEmpty()) {
            int start = q.poll();
            System.out.print(start);
            System.out.print(" ");
            ArrayList<Integer> adjs = adj.get(start);
            for(i=0; i<adjs.size(); i++) {
                int next = adjs.get(i);
                if (!visited[next]) {
                    q.offer(next);
                    visited[next] = true;
                }
            }
        }    
     }
}

