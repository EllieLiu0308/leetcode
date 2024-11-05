class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mincurr = nums[0]
        maxcurr = nums[0]
        maxhis = nums[0]

        for i in nums[1:]:
            maxcurr = max(maxcurr*i, mincurr*i,i)
            mincurr = min(mincurr*i, maxcurr*i,i)
            maxhis = max(maxcurr, maxhis)

        return maxhis