class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0

        while left < right:
            currentarea = min(height[left], height[right])* (right - left)
            maxarea = max(currentarea, maxarea)
        
            if height[left]> height[right]:
                right = right - 1
            else:
                left = left + 1
        
        return maxarea
                