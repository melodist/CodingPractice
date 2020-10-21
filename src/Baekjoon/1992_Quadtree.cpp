"""
https://www.acmicpc.net/problem/1992
Using divide and conquer
"""
#1. My Solution
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string compress(int r_s, int r_e, int c_s, int c_e, vector <vector <int>> &arr) 
{
    if (r_s == r_e){
        string ret = to_string(arr[r_s][c_s]);
        return ret;
    }
    
    int r_mid = (r_s + r_e) / 2;
    int c_mid = (c_s + c_e) / 2;
    string s_0 = compress(r_s, r_mid, c_s, c_mid, arr);
    string s_1 = compress(r_s, r_mid, c_mid+1, c_e, arr);
    string s_2 = compress(r_mid+1, r_e, c_s, c_mid, arr);
    string s_3 = compress(r_mid+1, r_e, c_mid+1, c_e, arr);
    
    string all0 = "0000";
    string all1 = "1111";

    string ret = s_0 + s_1 + s_2 + s_3;

    if (ret == all0) {
        ret = "0";
    }
    else if (ret == all1) {
        ret = "1";
    }
    else {
        string left = "(";
        string right = ")";
        ret = left + ret + right;
    }
    return ret;
}

int main()
{
   int n;
   scanf("%d", &n);
   vector <vector <int>> arr(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            arr[i][j] = s[j] - '0';
            
        }
    }
   
   string ans = compress(0, n-1, 0, n-1, arr);
   printf("%s", ans.c_str());
   
   return 0;
}
