class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict = {}
        i = 0
        while i < len(nums):
            if sum_dict.get(target - nums[i]) is not None:
                return [i, sum_dict.get(target - nums[i])]
            else:
                sum_dict[nums[i]] = i
            i = i+1
        return []


def main():
    nums = [2, 11, 7, 15]
    target = 9
    solution = Solution().twoSum(nums, target)
    print(solution)


if __name__ == '__main__':
    main()