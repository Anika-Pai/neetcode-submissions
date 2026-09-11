class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                maxSeq = max(length, maxSeq)
            
        return maxSeq