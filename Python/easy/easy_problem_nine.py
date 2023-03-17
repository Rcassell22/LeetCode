

class EasyProblemNine:
    '''
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

def main():
    test_x_1 = 121
    print('Test Case 1: Expected = True, Actual = ', EasyProblemNine.is_palindrome(test_x_1))

    test_x_2 = -121
    print('Test Case 1: Expected = False, Actual = ', EasyProblemNine.is_palindrome(test_x_2))

    test_x_3 = 10
    print('Test Case 1: Expected = False, Actual = ', EasyProblemNine.is_palindrome(test_x_3))

if __name__ == "__main__":
    main()