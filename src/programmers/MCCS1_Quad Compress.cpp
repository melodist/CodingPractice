"""
https://programmers.co.kr/learn/courses/30/lessons/68936
Using divide and conquer
"""
#include <string>
#include <vector>

using namespace std;

pair<int, int> func(int r_s, int r_e, int c_s, int c_e, vector<vector<int>> &arr) {    
    if (r_s == r_e) {
        if (arr[r_s][c_s] == 0) {
            return make_pair(1, 0);
        }
        else {
            return make_pair(0, 1);
        }
    }
    
    int r_mid = (r_s + r_e) / 2;
    int c_mid = (c_s + c_e) / 2;
    pair<int, int> v_lu = func(r_s, r_mid, c_s, c_mid, arr);
    pair<int, int> v_ru = func(r_s, r_mid, c_mid+1, c_e, arr);
    pair<int, int> v_ld = func(r_mid+1, r_e, c_s, c_mid, arr);
    pair<int, int> v_rd = func(r_mid+1, r_e, c_mid+1, c_e, arr);
    
    pair<int, int> ret;
    ret.first = v_lu.first + v_ru.first + v_ld.first + v_rd.first;
    ret.second = v_lu.second + v_ru.second + v_ld.second + v_rd.second;
        
    if (ret.first == 0) {
        return make_pair(0, 1);
    }
    else if (ret.second == 0) {
        return make_pair(1, 0);
    }
    else {
        return ret;
    }
}

vector<int> solution(vector<vector<int>> arr) {
    vector<int> answer;
    pair<int, int> ret;
    ret = func(0, arr.size()-1, 0, arr.size()-1, arr);
    answer.push_back(ret.first);
    answer.push_back(ret.second);
    return answer;
}
