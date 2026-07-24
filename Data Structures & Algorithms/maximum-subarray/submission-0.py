class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        best = nums[0]

        for num in nums:
            curr = max(num, curr + num)
            best = max(best, curr)

        return best