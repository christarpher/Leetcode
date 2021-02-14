class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        counter = 0
        if(nums):
            while(i < len(nums)):
                if(nums[i] == 0):
                    del nums[i]
                    counter += 1
                    i -= 1
                i += 1
            for i in range(counter):
                nums.append(0)
        return nums