class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        count = 0;
        for i in nums:
            if (i in hash):
                return True
            hash[i] = 1
        return False