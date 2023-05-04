class Solution(object):

    def fizz_buzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num = 1
        result = list()
        while num <= n:
            result.append(self.fizz_buzz_decider(num))
            num += 1
        return result


    def fizz_buzz_decider(self, n):
        """
        :type n: int
        :rtype: str
        """
        result_string = ""
        if n % 3 == 0 or n % 5 == 0:
            if n % 3 == 0:
                result_string += "Fizz"
            if n % 5 == 0:
                result_string += "Buzz"
        else:
            result_string = str(n)
        return result_string
