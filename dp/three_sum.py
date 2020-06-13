class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        three_sum_dict = set()
        three_sum = []
        for j in range(0, len(nums), 1):
            two_sum_set = self.twoSum(nums, -nums[j], j + 1)
            if two_sum_set:
                for two_sum in two_sum_set:
                    two_sum.append(nums[j])
                    two_sum.sort()
                    if str(two_sum) not in three_sum_dict:
                        three_sum.append(two_sum)
                        three_sum_dict.add(str(two_sum))
        return three_sum

    def twoSum(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict = {}
        i = start
        two_sum = []
        two_sum_set = set()
        while i < len(nums):
            if sum_dict.get(target - nums[i]) is not None:
                subset = [nums[i], sum_dict.get(target - nums[i])]
                if str(subset) not in two_sum_set:
                    two_sum.append(subset)
                    two_sum_set.add(str(subset))
            else:
                sum_dict[nums[i]] = nums[i]
            i = i + 1
        return two_sum


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution().threeSum(nums)
    print(solution)


if __name__ == '__main__':
    main()
