from typing import List

class EasyProblemOne:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        # for index_a, num_a in enumerate(nums):
        #     for index_b, num_b in enumerate(nums, start=index_a + 1):
        #         if num_a + num_b == target:
        #             return [index_a, index_b]
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if((nums[i] + nums[j]) == target):
                    return [i, j]
                else:
                    j = j + 1


def main():
    test_nums_1 = [2, 7, 11, 15]
    test_target_1 = 9
    print('Test Case 1:', EasyProblemOne.two_sum(test_nums_1, test_target_1))

    test_nums_2 = [3, 2, 4]
    test_target_2 = 6
    print('Test Case 2:', EasyProblemOne.two_sum(test_nums_2, test_target_2))

    test_nums_3 = [3, 3]
    test_target_3 = 6
    print('Test Case 2:', EasyProblemOne.two_sum(test_nums_3, test_target_3))

if __name__ == "__main__":
    main()


