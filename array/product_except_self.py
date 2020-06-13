class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_dict = {}
        product_dict[self.get_key(0, 'pre')] = 1
        product_dict[self.get_key(len(nums)-1, 'suf')] = 1
        i=1
        while i < len(nums):
            product_dict[self.get_key(i, 'pre')] = product_dict.get(self.get_key(i-1, 'pre')) * nums[i-1]

            product_dict[self.get_key(len(nums)-1-i, 'suf')] = \
                product_dict.get(self.get_key(len(nums)-i, 'suf')) * nums[len(nums)-i]
            i=i+1
        result = []
        i=0
        while i < len(nums):
            result.append(product_dict.get(self.get_key(i, 'pre')) * product_dict.get(self.get_key(i, 'suf')) )
            i = i+1
        return result

    def get_key(self, i, direction):
        return str(str(i) + direction)


def main():
    nums = [1,2,3,4]
    solution = Solution().productExceptSelf(nums)
    print(solution)


if __name__ == '__main__':
    main()