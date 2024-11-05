"""

EquiLeader

Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.



A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].


"""

from collections import Counter


def solution(A):

    N = len(A)

    # Handle the case where the array is empty
    if N == 0:
        return 0

    # Count occurrences of each element
    count = Counter(A)

    # Find the leader (if it exists)
    leader = None
    for key, value in count.items():
        if value > N // 2:
            leader = key
            break

    # No leader exists
    if leader is None:
        return 0

    # Count equi leaders
    equi_leaders_count = 0
    left_leader_count = 0

    # Loop until N-1 to consider S < N-1
    for i in range(N - 1):
        if A[i] == leader:
            left_leader_count += 1

        left_length = i + 1
        right_length = N - left_length
        right_leader_count = count[leader] - left_leader_count

        # Check if they are leaders in their segments
        if left_leader_count > left_length // 2 and right_leader_count > right_length // 2:
            equi_leaders_count += 1

    return equi_leaders_count


A = [4, 3, 4, 4, 4, 2]

print(solution(A))


# Without a Counter Method ;

def solution(A):

    N = len(A)

    # Find the leader of the entire array (if it exists)
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

    # Verify if the candidate is really a leader
    leader = -1
    leader_count = 0
    for number in A:
        if number == candidate:
            leader_count += 1

    if leader_count > N // 2:
        leader = candidate
    else:
        return 0  # No leader found, hence no equiLeaders

    # Count equiLeaders
    equi_leaders_count = 0
    left_leader_count = 0

    # Loop until N-1 to consider S < N-1
    for i in range(N - 1):
        if A[i] == leader:
            left_leader_count += 1

        left_length = i + 1
        right_length = N - left_length

        # Check if they are leaders in their segments
        if left_leader_count > left_length // 2 and (leader_count - left_leader_count) > right_length // 2:
            equi_leaders_count += 1

    return equi_leaders_count
