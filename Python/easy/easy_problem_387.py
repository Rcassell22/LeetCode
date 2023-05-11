class Solution(object):
    def first_uniq_char(self, s):
        """
        :type s: str
        :rtype: int

        Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

        This one is pretty inefficient but the point of these is I try and do them off the top of my head
        and as fast as I can. Should probably come back and do better at some point.
        """
        first_uniq_char_index = -1
        for index in range(0, len(s)):
            if s.count(s[index]) == 1:
                first_uniq_char_index = index
                break
        return first_uniq_char_index
