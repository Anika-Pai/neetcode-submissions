class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen = set()
        res = []

        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                tsum = nums[i] + nums[l] + nums[r]

                if tsum < 0:
                    l += 1
                elif tsum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
        return res



