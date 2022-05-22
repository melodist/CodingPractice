"""
https://leetcode.com/contest/weekly-contest-294/problems/minimum-lines-to-represent-a-line-chart
Weekly Contest 294
Implementation Problem
"""
#1. Solution using GCD (2209ms)
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        lines = len(stockPrices) - 1
        
        stockPrices.sort(key=lambda x: x[0])
        prev_dx, prev_dy = 0, 0
        
        for i in range(1, len(stockPrices)):
            prev_x, prev_y = stockPrices[i-1]
            x, y = stockPrices[i]
            dx = x - prev_x
            dy = y - prev_y
            gcd_dxdy = math.gcd(dx, dy)

            if i > 1 and dx // gcd_dxdy == prev_dx and dy // gcd_dxdy == prev_dy:
                lines -= 1
                
            prev_dx, prev_dy = dx // gcd_dxdy, dy // gcd_dxdy
            
        return lines
  
#2. Solution using Decimal (2033ms)
from decimal import *


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        lines = 1
        
        stockPrices.sort(key=lambda x: x[0])
        prev_slope = Decimal(0)
        
        for i in range(1, len(stockPrices)):
            prev_x, prev_y = stockPrices[i-1]
            x, y = stockPrices[i]
            slope = Decimal(y - prev_y) / Decimal(x - prev_x)

            if i > 1 and slope != prev_slope:
                lines += 1
                
            prev_slope = slope
            
        return lines if len(stockPrices) > 1 else 0
