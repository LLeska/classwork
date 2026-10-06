class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        return best