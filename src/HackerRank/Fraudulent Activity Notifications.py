"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
Using counting sort
"""
#1. My Solution
def activityNotifications(expenditure, d):
    # Number of notifications
    ans = 0

    # Set midpoints for median calculation
    i1, i2 = math.floor((d-1)/2), math.ceil((d-1)/2)

    # Initialize count sorted subarray
    cs = [0] * 201
    for i in range(d-1, -1, -1): 
        cs[expenditure[i]] += 1

    # Iterate through expenditures
    for i in range(d, len(expenditure)):
        # Find median
        j = k = 0
        while k <= i1:
            m1 = j
            k += cs[j]
            j += 1
            
        j = k = 0
        while k <= i2:
            m2 = j
            k += cs[j]
            j += 1

        m = (m1 + m2) / 2

        # Check if notification is given
        if expenditure[i] >= m * 2: ans += 1

        # Replace subarray elements
        cs[expenditure[i-d]] -= 1
        cs[expenditure[i]] += 1


    return ans
