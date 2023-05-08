class Solution:
    '''
    :type x: int
    :rtype: bool

    Given an integer x, return true if x is a palindrome, and false otherwise.
    '''
    @staticmethod
    def is_palindrome(x: int) -> bool:
        original_num = x
        reverse_num = 0
        palindrome = False
        # use modulo operator to keep chopping the last digit off
        # and create a reverse of the provided number.
        while x > 0:
            last_digit = x % 10
            reverse_num = (reverse_num * 10) + last_digit
            x = x - last_digit
            x = x / 10
        if original_num == reverse_num:
            palindrome = True
        return palindrome
