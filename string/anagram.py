from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = Counter(s)
        t_dict = Counter(t)
        if len(s_dict) != len(t_dict):
            return False
        for key in s_dict:
            if key not in t_dict or t_dict[key] != s_dict[key]:
                return False
        return True


def main():
    s, t = "anagram", "nagaram"
    solution = Solution().isAnagram(s, t)
    print solution


if __name__ == '__main__':
    main()
