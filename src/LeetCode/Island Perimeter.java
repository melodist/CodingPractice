/**
 * https://leetcode.com/problems/island-perimeter/
 * Flood Fill
 */
 //1. My Solution
 class Solution {
    public int islandPerimeter(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int ans = 0;
        
        for (int y=0; y<row; y++) {
            for (int x=0; x<col; x++) {
                if (grid[y][x] == 1) {
                    int temp = 4;
                    if (y-1 >= 0 && grid[y-1][x] == 1) temp -= 2;
                    if (x-1 >= 0 && grid[y][x-1] == 1) temp -= 2;
                    ans += temp;
                }
                
            }
        }
        
        return ans;
    }
}
