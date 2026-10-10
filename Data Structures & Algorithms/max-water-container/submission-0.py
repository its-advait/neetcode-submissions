class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            a = (min(height[left], height[right]) * (right-left))
            maxArea = max(a, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea