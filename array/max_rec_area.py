class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        min_idx = min(range(len(heights)), key=heights.__getitem__)
        this_area = len(heights) * heights[min_idx]
        left_area = self.largestRectangleArea(heights[:min_idx])
        right_area = self.largestRectangleArea(heights[(min_idx+1):])
        return max(this_area, left_area, right_area)


def main():
    nums = [2,1,5,6,2,3]
    solution = Solution().largestRectangleArea(nums)
    print(solution)


if __name__ == '__main__':
    main()