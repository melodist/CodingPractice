"""
Using BFS
"""
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int bfs(int i, int j, int **matrix, vector <vector<bool>> &visited, int n) {
	int ret = 0;
	queue <pair<int, int>> q;
	q.push(make_pair(i, j));
	visited[i][j] = true;
	
	while (!q.empty()){
		pair <int, int> p = q.front();
		q.pop();
		ret++;
		int y = p.first;
		int x = p.second;
		
		if (x+1 < n && matrix[y][x+1] == 1 && !visited[y][x+1]) {
			q.push(make_pair(y, x+1));
			visited[y][x+1] = true;
		}
		
		if (y+1 < n && matrix[y+1][x] == 1 && !visited[y+1][x]) {
			q.push(make_pair(y+1, x));
			visited[y+1][x] = true;
		}
		
		if (x-1 >= 0 && matrix[y][x-1] == 1 && !visited[y][x-1]) {
			q.push(make_pair(y, x-1));
			visited[y][x-1] = true;
		}
		
		if (y-1 >= 0 && matrix[y-1][x] == 1 && !visited[y-1][x]) {
			q.push(make_pair(y-1, x));
			visited[y-1][x] = true;
		}
	}
	return ret;
}

void solution(int sizeOfMatrix, int **matrix) {
	vector <vector <bool>> visited(sizeOfMatrix, vector<bool> (sizeOfMatrix, false));
	int regions = 0;
	int count;
	vector <int> r;
	
	for (int i = 0; i < sizeOfMatrix; i++) {
		for (int j = 0; j < sizeOfMatrix; j++) {
			if (matrix[i][j] == 1 && !visited[i][j]) {
				count = bfs(i, j, matrix, visited, sizeOfMatrix);
				regions++;
				r.push_back(count);
			}
		}
	}
	
	sort(r.begin(), r.end());
	if (regions == 0) {
		printf("%d", 0);
	}
	
	else {
		cout << regions << endl;
		for (int i = 0; i < r.size(); i++) {
			cout << r[i] << " ";
		}
	}	
}
