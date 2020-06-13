from collections import Counter, defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for char in s:
                char_count[ord(char) - ord('a')] += 1
            result[tuple(char_count)].append(s)
        return result.values()


def main():
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution().groupAnagrams(arr)
    print solution


if __name__ == '__main__':
    main()
