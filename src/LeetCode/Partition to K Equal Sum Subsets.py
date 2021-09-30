"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/640/week-5-september-29th-september-30th/3993/
Using backtracking
"""
#1. My Solution
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, curIdx, limitIdx):
            if subsetSum[curIdx] == subset:

                """ current index (K - 2) represents (K - 1) 
                subsets of equal sum last partition will 
                already remain with sum 'subset'"""
                if (curIdx == K - 2):
                    return True

                # recursive call for next subsetition 
                return isKPartitionPossibleRec(arr, subsetSum, taken, 
                                               subset, K, N, curIdx + 1 , N - 1)

            # start from limitIdx and include 
            # elements into current partition 
            for i in range(limitIdx, -1, -1):

                # if already taken, continue 
                if (taken[i]):
                    continue
                tmp = subsetSum[curIdx] + arr[i] 

                # if temp is less than subset, then only 
                # include the element and call recursively 
                if (tmp <= subset):

                    # mark the element and include into 
                    # current partition sum 
                    taken[i] = True
                    subsetSum[curIdx] += arr[i] 
                    nxt = isKPartitionPossibleRec(arr, subsetSum, taken, 
                                                  subset, K, N, curIdx, i - 1)

                    # after recursive call unmark the element and 
                    # remove from subsetition sum 
                    taken[i] = False
                    subsetSum[curIdx] -= arr[i] 
                    if (nxt):
                        return True
            return False
  
        n = len(nums)
        # If K is 1,
        # then complete array will be our answer 
        if (k == 1):
            return True

        # if array sum is not divisible by K then 
        # we can't divide array into K partitions 
        sum_nums = sum(nums)
        if (sum_nums % k != 0):
            return False

        # the sum of each subset should be subset (= sum / K) 
        subset = sum_nums // k 

        # Initialize sum of each subset from 0 
        subsetSum = [0] * k

        # mark all elements as not taken 
        taken = [False] * n

        # initialize first subsubset sum as  
        # last element of array and mark that as taken 
        subsetSum[0] = nums[n - 1] 
        taken[n - 1] = True

        # call recursive method to check 
        # K-substitution condition 
        return isKPartitionPossibleRec(nums, subsetSum, taken, subset, k, n, 0, n - 1)
    
#2. Other Solution
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(i, count, total):
            if count == k:
                return True
            
            if total > target_sum:
                return False
            
            if total == target_sum:
                return backtrack(0, count + 1, 0)
            
            for j in range(i, n):
                if j not in taken:
                    taken.add(j)
                    
                    if backtrack(j + 1, count, nums[j] + total):
                        return True
                    
                    taken.remove(j)
                
            return False
        
        n = len(nums)
        total = sum(nums)
        
        if total % k != 0:
            return False
        
        target_sum = total // k
        taken = set()
        nums.sort(reverse=True)
        memo = {}
        
        return backtrack(0, 0, 0)
