"""
PermMissingElem

Find the missing element in a given permutation

An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)],
 which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].

"""


def solution(A):

    if len(A) == 0 or sorted(A)[0] != 1:
        return 1

    A.sort()

    for index, value in enumerate(A):

        if index + 1 != value:
            return index + 1

    return A [-1] + 1

"""

def solution(A):

    A_len = len(A)
    arr = [0] * (A_len+1)
    
    for el in A:
        arr[el-1] = 1 # array 0 based
    
    for i, item in enumerate(arr):
        if item == 0:
            return i+1 # bring back the value
    return -1


"""

"""

def solution(A):
    N = len(A)
    return (((N + 1) * ((N + 1) + 1) // 2) - sum(A))


"""

"""

def solution(A):

    if (len(A) == 0):
        return 1

    A.sort()
    for index, digit in enumerate(A):
        if index+1 != digit and len(A) >= index+1:
            return index+1

    return A[len(A)-1]+1

"""


"""

def solution(A):
    missing_element = len(A)+1
    for idx,value in enumerate(A):
        missing_element = missing_element ^ value ^ (idx+1)
    return missing_element


"""