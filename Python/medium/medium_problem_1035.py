class Solution(object):
    def max_uncrossed_lines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int

        Daily question May 11.

        Ran out of time, so used CodeGPT (GPT3.5 Turbo) to solve the problem. As usual,
        I just used the problem description with a minor tweak to explicitly ask it for a python
        function. I also gave it a few-shot exemplar of the first test case and expected result.
        Works well, and beat 80% of submissions in runtime.
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]