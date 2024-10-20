"""

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].



"""


def solution(A):

    # Create a set of positive integers in A
    positive_set = set(x for x in A if x > 0)

    # Check for the smallest positive integer not in the set
    for i in range(1, len(A) + 2):  # We need to check up to len(A) + 1

        if i not in positive_set:
            return i

    # This line should never be reached given the problem constraints
    return len(A) + 2


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-3, -1]))
