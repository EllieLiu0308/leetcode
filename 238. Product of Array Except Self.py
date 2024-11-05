class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]* len(nums)

        left = 1
        for i in range (0, len(nums)):
            output[i] = output[i]* left
            left = left*nums[i]          

        right = 1
        for i in range (len(nums)-1,-1,-1):
            output[i] = output[i]* right
            right = right*nums[i]          

        return output