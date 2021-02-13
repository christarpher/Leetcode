class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while(j < len(nums)):
            if(nums[i] == nums[j]):
                del nums[j]
            else:
                i += 1
                j = i + 1