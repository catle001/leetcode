class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_dict = {}
        for i in nums:
            if hash_dict.get(i) == True:
                return True
            else:
                hash_dict[i] = True
        return False


def main():
    nums = [2, 11, 7, 15]
    solution = Solution().containsDuplicate(nums)
    print(solution)


if __name__ == '__main__':
    main()