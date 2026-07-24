class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cnum = 0 
        nums.sort()

        for i in range(len(nums)): 
            if cnum != nums[i]:
                break
            
            cnum+=1
        
        return cnum