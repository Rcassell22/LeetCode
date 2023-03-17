class Solution(object):
    """
    Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
    """
    def convert_to_title(self, column_number):
        """
        :type column_number: int
        :rtype: str
        """
        unicode_diff = 65 # dec code for 'A'
        alphabet_count = 26 # num letters in the alphabet
        final_letter = ""
        while column_number > 0:
            # Need to subtract 1 since we get the remainder first, otherwise
            # we'll always get 0 with the floor division.
            column_number -= 1
            second_letter_num = column_number % alphabet_count
            second_letter = chr(second_letter_num + unicode_diff)
            final_letter = second_letter + final_letter
            column_number //= alphabet_count
        return final_letter
