class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if j == len(s):
                return True
        return False


def main():
    s = "abc"
    t = "ahbgdc"
    solution = Solution().isSubsequence(s, t)
    print(solution)


if __name__ == '__main__':
    main()