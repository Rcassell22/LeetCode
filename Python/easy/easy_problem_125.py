class Solution(object):
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
    all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_palindrome = False
        formatted_string = self.strip_non_alphanumeric_characters(s).lower()
        formatted_string_reverse = formatted_string[len(formatted_string)::-1]
        if formatted_string == formatted_string_reverse:
            is_palindrome = True
        return is_palindrome

    def strip_non_alphanumeric_characters(self, string):
        """
        Given a string, remove any non-alphanumric characters before returning the string
        """
        stripped_string = ""
        for char in string:
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
                stripped_string += char
        return stripped_string
