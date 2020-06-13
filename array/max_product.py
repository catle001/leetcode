import sys

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_here = max_here = max_arr = nums[0]
        for i in range(1, len(nums), 1):
            #switch when num<0
            if nums[i] < 0:
                max_here, min_here = min_here, max_here

            max_here = max(nums[i], max_here * nums[i])
            min_here = min(nums[i], min_here * nums[i])

            max_arr = max(max_here, max_arr)
        return max_arr


def main():
    nums = [2,3,-2,4]
    solution = Solution().maxProduct(nums)
    print(solution)


if __name__ == '__main__':
    main()