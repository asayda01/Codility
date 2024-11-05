"""

Dominator
Find an index of an array such that its value occurs at more than half of indices in the array.

An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].


"""

from collections import Counter


def solution(A):
    # Handle the case where the array is empty
    if len(A) == 0: return -1

    # Initialise a Counter method
    a = Counter(A).most_common(1)[0]
    dominator_value, count = a

    # Check if the count exceeds N // 2
    if count <= len(A) // 2: return -1

    # Return the index of the first occurrence of the dominator
    for index in range(len(A)):
        if A[index] == dominator_value:
            return index

    # Fallback, should not reach here
    return -1


# Without a Counter Method ;


def solution(A):
    N = len(A)

    # Handle the case where the array is empty
    if N == 0:
        return -1

    # Find a candidate for the dominator
    candidate = None
    count = 0

    for number in A:
        if count == 0:
            candidate = number
            count = 1
        elif number == candidate:
            count += 1
        else:
            count -= 1

    # Validate the candidate
    if candidate is not None:
        count = 0
        for number in A:
            if number == candidate:
                count += 1

        # Check if the candidate is indeed a dominator
        if count > N // 2:
            # Find the index of the first occurrence
            for index in range(N):
                if A[index] == candidate:
                    return index

    # No dominator found
    return -1
