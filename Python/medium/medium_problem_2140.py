class Solution(object):
    """
    :type questions: List[List[int]]
    :rtype: int

    Daily Problem May 12th, 2023.

    This one was hard. Not only did I not solve it in the time limit on my own, but
    I had to spend about 2 hours writing prompts to get GPT to solve it correctly.
    What it seemed to have the hardest time with was the concept of brainpower. Once I
    did a better job of explaining that, it gave me an answer that worked, but was two slow.
    After that, I kept asking it to make it faster, and eventually it just kept giving me the same
    solution. So I asked it to use recursion AND dynamic programming, which strangely it didn't do,
    BUT it came up with a solution that was fast and actually worked. At the bottom of this file
    I put the initial prompt I used that gave me the first solution that actually worked, but was too slow.

    All in all I got a lot of good prompt engineering practice. Need to study some dynamic programming though,
    because this seems pretty straightforward.

    """
    def most_points(self, questions):
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            points, skip = questions[i]
            sub_questions_start = i + skip + 1
            sub_score = 0
            if sub_questions_start < n:
                sub_score = dp[sub_questions_start]
            dp[i] = max(points + sub_score, dp[i+1])
        return dp[0]

    # def most_points(self, questions):
    #     """
    #     :type questions: List[List[int]]
    #     :rtype: int
    #     """
    #     # This works but takes too long
    #     # n = len(questions)
    #     # if n == 0:
    #     #     return 0
    #     # max_score = 0
    #     # for i in range(n):
    #     #     points, skip = questions[i]
    #     #     sub_questions = questions[i+skip+1:]
    #     #     score = points + self.most_points(sub_questions)
    #     #     max_score = max(max_score, score)
    #     # return max_score

    # This also worked, and was faster, but still too slow.
    # def most_points_helper(self, questions, memo):
    #     n = len(questions)
    #     if n == 0:
    #         return 0
    #     if n in memo:
    #         return memo[n]
    #     max_score = 0
    #     for i in range(n):
    #         points, skip = questions[i]
    #         sub_questions = questions[i+skip+1:]
    #         score = points + self.most_points_helper(sub_questions, memo)
    #         max_score = max(max_score, score)
    #     memo[n] = max_score
    #     return max_score

    # def most_points(self, questions):
    #     """
    #     :type questions: List[List[int]]
    #     :rtype: int
    #     """
    #     memo = {}
    #     return self.most_points_helper(questions, memo)

    # Still faster, but not fast enough
    # def most_points_helper(self, questions, start, memo):
    #     n = len(questions)
    #     if n == start:
    #         return 0
    #     if start in memo:
    #         return memo[start]
    #     max_score = 0
    #     for i in range(start, n):
    #         points, skip = questions[i]
    #         sub_questions_start = i + skip + 1
    #         if sub_questions_start in memo:
    #             sub_score = memo[sub_questions_start]
    #         else:
    #             sub_score = self.most_points_helper(questions, sub_questions_start, memo)
    #         score = points + sub_score
    #         if score > max_score:
    #             max_score = score
    #     memo[start] = max_score
    #     return max_score

    # def most_points(self, questions):
    #     """
    #     :type questions: List[List[int]]
    #     :rtype: int
    #     """
    #     memo = {}
    #     return self.most_points_helper(questions, 0, memo)


'''
You are given a 0-indexed 2D integer array called questions where questions[i] = the question, questions[i][0] = the number of points for the question, and questions[i][1] = the amount of brainpower required to answer the question.
The value for brainpower is the number of questions you have to skip after choosing that question.
For example if questions = [[3,2],[4,3],[4,4],[2,5]], and you pick questions[0], you will get 3 points, and have to skip 2 questions, because questions[0][0] = 3, and questions[0][1] = 2.
We want to loop through questions, keep count of how many points we get, and we want to pick the questions that will give us the greatest number of points. Keep looping through the questions until we determine the greatest number of points, and return that value.
Do not sort questions.

Example 1: If questions = [[3,2],[4,3],[4,4],[2,5]], The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points because questions[0][0] = 3. You will be unable to solve the next 2 questions becasue questions[0][1] = 2
- Solve question 3: Earn 2 points because questions[3][0] = 2.
- The total points is now 5 because 2 points plus 3 points equals 5 points.
There is no other way to earn 5 or more points, so the function should return our total of 5 points.

Example 2: If questions = [[1,1],[2,2],[3,3],[4,4],[5,5]], the maximum points can be earned by solving questions 1 and 4.
- Skip question 0.
- Solve question 1: Earn 2 points because questions[1][0] = 2. We will be unable to solve the next 2 questions because questions[1][1] = 2
- Solve question 4: Earn 5 points because questions[4][0] = 5.
- The total points is now 7 because 2 points plus 5 points equals 7 points.
There is no other way to earn 7 or more points, so the function should return our total of 7 points.

Example 3: If questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]], the total points you can ear is 157, so the function should return 157.


'''