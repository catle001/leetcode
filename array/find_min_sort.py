class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        c = len(nums) - 1
        while a < c:
            b = (a + c) / 2
            if nums[b] == nums[c]:
                c = c -1
            elif nums[b] > nums[c]:
                a = b + 1
            else:
                c = b
        return nums[c]


def main():
    nums = [3, 4, 5, 1, 2]
    solution = Solution().findMin(nums)
    print(solution)


if __name__ == '__main__':
    main()
