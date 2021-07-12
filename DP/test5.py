class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        arr = sorted(list(set(nums)))
        n = len(arr) + 1
        k = len(nums) + 1
        lst = [[0] * k for i in range(n)]
        for i in range(1, len(lst)):
            for j in range(1, len(lst[0])):
                if arr[i - 1] == nums[j - 1]:
                    lst[i][j] = 1 + lst[i - 1][j - 1]
                else:
                    lst[i][j] = max(lst[i - 1][j], lst[i][j - 1])
        return lst[-1][-1]
