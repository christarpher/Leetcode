class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) > 2:
            nums.sort()
            index = 0
            while(index < len(nums)-2):
                if(nums[index] == nums[index+1]):
                    index += 2
                else:
                    return nums[index]
            return nums[index]
                
        else:
            return nums[0]