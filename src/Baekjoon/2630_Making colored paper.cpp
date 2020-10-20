"""
https://www.acmicpc.net/problem/2630
Using divide and conquer
"""
#1. My Solution
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

pair <int, int> func(int r_s, int r_e, int c_s, int c_e, vector <vector <int>> &arr) 
{
    if (r_s == r_e)
    {
        if (arr[r_s][c_s] == 0)
        {
            return make_pair(1, 0);
        }
        else
        {
            return make_pair(0, 1);
        }
    }
    
    int r_mid = (r_s + r_e) / 2;
    int c_mid = (c_s + c_e) / 2;
    pair <int, int> p_lu = func(r_s, r_mid, c_s, c_mid, arr);
    pair <int, int> p_ru = func(r_s, r_mid, c_mid+1, c_e, arr);
    pair <int, int> p_ld = func(r_mid+1, r_e, c_s, c_mid, arr);
    pair <int, int> p_rd = func(r_mid+1, r_e, c_mid+1, c_e, arr);
    
    int total_0 = p_lu.first + p_ru.first + p_ld.first + p_rd.first;
    int total_1 = p_lu.second + p_ru.second + p_ld.second + p_rd.second;
    
    if (total_0 == 0)
    {
        return make_pair(0, 1);
    }
    else if (total_1 == 0)
    {
        return make_pair(1, 0);
    }
    else
    {
        return make_pair(total_0, total_1);
    }
}

int main()
{
    int n;
    cin >> n;
    string s;
    getline(cin, s);
    vector <vector <int>> arr(n, vector<int>(n, 0));
    
    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s);
        
        string temp;
        stringstream ss(s);
        int j = 0;
        while (getline(ss, temp, ' ')) {
            arr[i][j++] = atoi(temp.c_str());
        }
    }
    
    pair <int, int> ans = func(0, n-1, 0, n-1, arr);
    cout << ans.first << endl;
    cout << ans.second << endl;
    
    return 0;
}

#2. Other Solution
#include <stdio.h>
int cnt_w = 0, cnt_b = 0;
void dfs(int arr[][128], int s_x, int s_y, int e_x, int e_y) {
	int block_type = arr[s_x][s_y], escape = 0;
	for(int y = s_y; y <= e_y; y++) {
		for(int x = s_x; x <= e_x; x++)
			if(arr[x][y] != block_type) 
				escape = 1;
		if(escape) break;
	}
	if(escape) {
		int mid_x = (s_x + e_x) / 2;
		int mid_y = (s_y + e_y) / 2;
		dfs(arr, s_x, s_y, mid_x, mid_y);
		dfs(arr, mid_x + 1, s_y, e_x, mid_y);
		dfs(arr, s_x, mid_y + 1, mid_x, e_y);
		dfs(arr, mid_x + 1, mid_y + 1, e_x, e_y);
	}
	else {
		if(block_type) cnt_b++;
		else cnt_w++;
	}
}

int main() {
	int n, arr[128][128] = {0,};
	scanf("%d", &n);
	for(int y = 0; y < n; y++)
		for(int x = 0; x < n; x++)
			scanf("%d", &arr[x][y]);
	dfs(arr, 0, 0, n-1, n-1);
	printf("%d\n%d\n", cnt_w, cnt_b);
	return 0;
}
