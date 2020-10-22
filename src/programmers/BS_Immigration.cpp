"""
https://programmers.co.kr/learn/courses/30/lessons/43238?language=cpp
Using binary search
"""
#1. My Solution
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool binary_search(vector <int> times, long long ans, long long n) {
    long long count = 0;
    for (auto t: times) {
        count += ans / t;
    }
    
    if (count >= n) {
        return true;
    }
    
    return false;
}

long long solution(int n, vector<int> times) {
    sort(times.begin(), times.end());
    long long left, right, mid;
    left = 0;
    right = 1E15;
    
    while (left <= right) {
        mid = (left + right) / 2;
        
        if (binary_search(times, mid, n)) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }   
    }
    
    return left;
}
