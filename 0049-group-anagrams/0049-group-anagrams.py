from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            anagram[key].append(word)
        return list(anagram.values())