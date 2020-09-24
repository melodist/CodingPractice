/*
https://www.acmicpc.net/problem/1967
Using BFS
*/
// My Solution
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;
 
int n;
int visited[10002]={0};
vector<pair<int,int>> node[10002];
 
int ans=0;
int end_point=0;
void bfs(int start){ 
    queue<pair<int, int>> q; 
    q.push(make_pair(start, 0)); 
    visited[start] = true; 
        while(!q.empty()){ 
            pair<int, int> p = q.front(); 
            q.pop(); 
            int x, dist;
            x = p.first;
            dist = p.second;
           if(ans<dist){
                ans=dist;
                end_point=x;
            }

            for(int i=0; i< node[x].size(); i++){
                int y = node[x][i].first;
                int next_dist = node[x][i].second;
                if(!visited[y]){
                    q.push(make_pair(y, dist + next_dist)); 
                    visited[y] = true; 
            } 
        } 
    } 
}

int main(){
    
    cin>>n;
    
    int parent,child,length;
    for(int i=0;i<n-1;i++){
        scanf("%d %d %d",&parent,&child,&length);
        node[parent].push_back(make_pair(child,length));
        node[child].push_back(make_pair(parent,length));
    }
    
    //가장 멀리 있는 정점(end_point) 구하기
    bfs(1);
    
    ans=0;
    memset(visited,0,sizeof(visited));
    
    //end_point와 가장 멀리 있는 정점과의 거리 구하기
    bfs(end_point);
    cout<<ans<<endl;

    return 0;
}
