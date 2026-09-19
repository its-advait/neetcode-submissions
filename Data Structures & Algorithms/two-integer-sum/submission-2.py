class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            t = target - num
            if t in d and d[t] != i:
                return [d[t], i]
            d[num] = i