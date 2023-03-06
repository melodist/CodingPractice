"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
Using binary search
"""
#1. My Solution (627ms)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights) + 1

        while left < right:
            mid = (left + right) // 2

            k = 1
            temp = 0
            for w in weights:
                if temp + w <= mid:
                    temp += w
                else:
                    k += 1
                    temp = w
                    
            if k <= days:
                right = mid
            else:
                left = mid + 1                

        return left
        
#2. Other Solution (438ms)
class Solution:
    def shipWithinDays(self, weights, D):
        def can_ship(capacity): #This is a random guess of capacity from mid 
            #Total_weight starts at zero 
            total_item_weight = 0
            #We aren't at day zero it's day 1 (since this is the first day of me adding it )
            #Up until we've been at capacity 
            cur_ship_days = 0 #No days shipped so far 
            
            for weight in weights:
                total_item_weight += weight 
                if total_item_weight > capacity: 
                    #If at capacity keep the cur_weight that broke it then (don't reset it back to zero) else you miss that weight day.
                    total_item_weight = weight #so keep the weight so we don't lose you. 
                    
                    cur_ship_days += 1 #The number of days then to ship packages of the PREVIOUS day now + 1 since it's exceeded capacity. Else if all is good
                    #Then cur_ship_days is just one. 
                    
            #So the reason why you need to do cur_ship_days + 1 is b/c
            # +1 is the total_item_weight = weight this ship_day is to be added as well since it broke capacity. 
            if cur_ship_days + 1 <= D: 
                return True
            else: #Not possible
                return False
            
        low, high = max(weights), sum(weights)
        while low < high:
                # guess the capacity of ship
            weight_capacity = low + (high - low) // 2
            if can_ship(weight_capacity): 
                high = weight_capacity
                    
            else: 
                low = weight_capacity + 1

        return low
