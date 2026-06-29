class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        match = [p for p in patterns if p in word]
        return len(match)
        
        # count = 0
        # for i in patterns:
        #     if i in word:
        #         count += 1
        
        # return count

