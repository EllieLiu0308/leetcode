class Solution:
    def maxSubArray(self, nums):
        ans = -inf
        for i in range(len(nums)):
            cursum = 0
            for j in range(i, len(nums)):
                cursum = cursum + nums[j]
                ans = max(ans, cursum)
        return ans

 




 