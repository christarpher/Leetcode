class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in table and i != table.get(complement):
                return [i, table.get(complement)]