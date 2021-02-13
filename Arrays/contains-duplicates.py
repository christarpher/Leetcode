class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) >= 2):
            nums.sort()
            i=1
            while(i < len(nums)):
                if(nums[i-1] == nums[i]):
                    return True
                else:
                    i += 1
            return False
        else:
            return False