"""
https://leetcode.com/problems/majority-element-ii/
문제 조건을 만족하는 수의 count는 loop를 마쳤을 때 무조건 양수가 됨
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = 0, 0
        v1, v2 = None, None
        for n in nums:
            if n == v1:
                c1 += 1
            elif n == v2:
                c2 += 1
            elif c1 == 0:
                v1, c1 = n, 1
            elif c2 == 0:
                v2, c2 = n, 1

            else:
                c1, c2 = c1-1, c2-1
                
        return [v for v in [v1, v2] if nums.count(v)>len(nums)/3]
