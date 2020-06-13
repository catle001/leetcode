class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rotate = self.find_rotate_point(nums)
        if len(nums) == 0:
            return -1
        if target <= nums[-1]:
            return self.search_sorted(nums, target, rotate, len(nums-1))
        else:
            return self.search_sorted(nums, target, 0, rotate)

    def search_sorted(self, nums, target, start, end):
        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid

        if nums[end] == target:
            return end
        else:
            return -1

    def find_rotate_point(self, nums):
        a = 0
        c = len(nums) - 1
        while a < c:
            b = (a + c) / 2
            if nums[b] == nums[c]:
                c = c - 1
            elif nums[b] > nums[c]:
                a = b + 1
            else:
                c = b
        return c


def main():
    nums = [1,3]
    target = 3
    solution = Solution().search(nums, target)
    print(solution)


if __name__ == '__main__':
    main()
