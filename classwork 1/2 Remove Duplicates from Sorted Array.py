class Solution(object):
    def removeDuplicates(self, nums):
        a = sorted(set(nums))
        nums[:len(a)] = a
        return len(a)