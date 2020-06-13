class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_arr = max_here = nums[0]
        for i in nums[1:]:
            if i > i + max_here:
                max_here = i
            else:
                max_here = i + max_here
            if max_here > max_arr:
                max_arr = max_here
        return max_arr


def main():
    nums = [1]
    solution = Solution().maxSubArray(nums)
    print(solution)


if __name__ == '__main__':
    main()