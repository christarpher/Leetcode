class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #yes, this is not the most efficient, but it's also easy to understand
        for i in range(k):
            nums.insert(0,nums.pop(len(nums)-1))
        