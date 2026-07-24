class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = { 0 : 1}
        curSum = 0
        count = 0

        for i, num in enumerate(nums):
            curSum += num
            prefix = curSum - k

            count += prefixSums.get(prefix, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return count