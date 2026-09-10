class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prod = math.prod(nums)
        prefix = 1

        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
            
