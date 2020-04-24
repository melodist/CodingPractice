"""
https://www.hackerrank.com/challenges/flatland-space-stations/problem
"""
def flatlandSpaceStations(n, c):
    flag = [0] * n
    for val in c:
        flag[val] = 1
    
    # Store distance from city to nearest station for one direction
    def calc(flag, n):
        dp = [0] * n
        for i in range(n):
            if flag[i] == 1:
                dp[i] = 0
            else:
                if i==0:
                    dp[i] = 10**9
                else:
                    dp[i] = dp[i-1] + 1

        return dp

    dp_left = calc(flag, n)
    dp_right = calc(flag[::-1], n)
    ans = 0
    
    for i, (a,b) in enumerate(zip(dp_left, dp_right[::-1])):
        ans = max(ans, min(a, b)) # Find the nearest distance for each city and find maximum distance for all cities.

    return ans
