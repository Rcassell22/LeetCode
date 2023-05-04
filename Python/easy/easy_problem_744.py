
class Solution(object):
    def next_greatest_letter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str

        You are given an array of characters "letters" that is sorted in non-decreasing order, and a character "target".
        There are at least two different characters in "letters".
        Return the smallest character in "letters" that is lexicographically greater than "target".
        If such a character does not exist, return the first character in "letters".
        """
        current_result = None
        target_ord = ord(target)
        for char in letters:
            char_ord = ord(char)
            if char_ord > target_ord:
                if current_result is None:
                    current_result = char
                else:
                    if char_ord < ord(current_result):
                        current_result = char
        if current_result is None:
            current_result = letters[0]
        return current_result