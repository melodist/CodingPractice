"""
https://www.acmicpc.net/problem/11279
Using maximum heap
C++ creates maximum heap for priority queue by default
"""
#1. My Solution
#include <iostream>
#include <queue>

using namespace std;

int main()
{
   priority_queue<int> pq;
   int n;
   scanf("%d", &n);
   for (int i = 0; i < n; i++) {
       int x;
       scanf("%d", &x);
       if (x > 0) {
           pq.push(x);
       }
       else {
           if (pq.empty()) {
               printf("%d\n", 0);
           }
           else {
               printf("%d\n", pq.top());
               pq.pop();
           }
       }
   }
   return 0;
}
