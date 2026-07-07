class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces
        s = s.rstrip()

        # Find the last word length
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            count += 1

        return count