class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max_len = 0
        for num in nums:
            if num not in dict:
                is_first = True if num-1 not in dict else False
                next_num = None if num+1 not in dict else dict[num+1]
                if next_num is not None:
                    next_num.is_first = False
                dict[num] = Node(is_first, next_num)
                if not is_first:
                    dict[num - 1].next = dict[num]
        for key in dict:
            here = dict[key]
            if here.is_first:
                len = 1
                while here.next is not None:
                    here = here.next
                    len += 1
                max_len = max(max_len, len)
        return max_len


class Node(object):
    def __init__(self, is_first, next):
        self.is_first = is_first
        self.next = next


def longestConsecutive(self, nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    numCourses = [100, 4, 200, 1, 3, 2]
    solution = Solution().longestConsecutive(numCourses)
    print(solution)


if __name__ == '__main__':
    main()