class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_length = 0

        for num in numbers:
            if num - 1 not in numbers:
                length = 1

                while num + length in numbers:
                    length += 1

                max_length = max(max_length, length)

        return max_length