class Subset:
    def __init__(self, list, sum, size):
        self.list = list
        self.sum = sum
        self.size = size

    def add(self, num):
        new_list = self.list + [num]
        new_sum = self.sum + num
        new_size = self.size + 1
        return Subset(new_list, new_sum, new_size)


class Solution(object):
    def __init__(self):
        self.size = 4
        self.dict = {} #[size,sum]:[]

    def fourSum(self, nums, target):



def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution().fourSum(nums, target)
    print(solution)



if __name__ == '__main__':
    main()