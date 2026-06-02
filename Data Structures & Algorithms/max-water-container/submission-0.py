class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        def get_container_volume():
            return min(heights[l], heights[r]) * (r - l)

        max_container = 0

        while l < r:
            cur_container = get_container_volume()

            max_container = max(cur_container, max_container)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_container

        