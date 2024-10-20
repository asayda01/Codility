"""


A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].


"""


def solution(nums):
    product = 1
    negative_sum = 0
    has_positive = False

    for num in nums:
        if num > 0:
            product *= num
            has_positive = True
        elif num < 0:
            negative_sum += abs(num)

    if not has_positive:
        return negative_sum  # If there are no positive numbers

    return product + negative_sum  # Return the combined result


# Example usage
input_data = [2, 100, 3, -1000]
result = solution(input_data)
print(result)  # Expected output: 600

print(solution([-3, 1, 2, -2, 5, 6])) # 60


## or

def solution(A):
    # Sort the array
    A_sorted = sorted(A)

    # Calculate the product of the three largest numbers
    max_product_1 = A_sorted[-1] * A_sorted[-2] * A_sorted[-3]

    # Calculate the product of the two smallest and the largest number
    max_product_2 = A_sorted[0] * A_sorted[1] * A_sorted[-1]

    # Return the maximum of the two products
    return max(max_product_1, max_product_2)
