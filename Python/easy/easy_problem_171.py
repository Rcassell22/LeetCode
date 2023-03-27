class Solution(object):
    def title_to_number(self, column_title):
        """
        Given a string column_title that represents the column title as appears in an Excel sheet,
        return its corresponding column number.
        :type column_title: str
        :rtype: int
        """
        alphabet_count = 26 # num letters in the alphabet
        unicode_diff = 65 # dec code for 'A'
        title_list = list(column_title)
        column_num = 0
        for char in title_list:
            column_num *= alphabet_count
            column_num += ord(char) - unicode_diff + 1
        return column_num