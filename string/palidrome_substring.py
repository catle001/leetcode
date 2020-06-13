class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = 0, 0, 0
        for i in range(len(s)):
            for this_len, j, l, r in [(0, 0, i, i+1), (1, 1, i, i)]:
                while l-j >= 0 and r+j < len(s) and s[l-j] == s[r+j]:
                    this_len += 2
                    j += 1
                if ans[0] < this_len:
                    ans = this_len, l-j+1, r+j-1
        return "" if ans[0] == 0 else s[ans[1] : ans[2]+1]

    def palindrome_count(self, s):
        count = 0
        palidrome_set = set()
        for i in range(len(s)):
            for l, r in [(i, i+1), (i, i)]:
                j = 0
                while l-j >= 0 and r+j < len(s) and s[l-j] == s[r+j]:
                    substring = s[l-j:r+j+1]
                    if substring not in palidrome_set:
                        count += 1
                        palidrome_set.add(substring)
                    j += 1
        return count


def main():
    s= "cbbd"
    solution = Solution().palindrome_count(s)
    print solution


if __name__ == '__main__':
    main()
