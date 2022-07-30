# Brute Force 2 for: O(n^2)


# Faster:  O(nlogn) or O(mlogm). n is number of array A, m is number of array B. Can reverse!
# Goal: Find B[j] closest to -A[i]
import sys
import bisect


def findSmallestDifference(A, B, m, n):

    # Sort both arrays
    # using sort function
    A.sort()
    B.sort()

    a = 0
    b = 0

    # Initialize result as max value
    res = sys.maxsize
    result = sys.maxsize

    while (a < m):
        # O(log(n)) -> Bisect method works on the concept of binary search
        # print("b: ", bisect.bisect_left(B, -A[a]))
        # print("B: ", bisect.bisect_right(B, -A[a]))
        res = min(abs(A[a]-B[bisect.bisect_left(B, -A[a])]),
                  abs(A[a]-B[bisect.bisect_right(B, -A[a])]))
        result = min(res, result)

        a += 1
    # Can try with: while(b < n): ...

    return result


if __name__ == "__main__":
    # Input given array A
    A = [1, 8, 2, 9]

    # Input given array B
    B = [-5, -6, 3, -7, -4]

    m = len(A)
    n = len(B)

    # dic_A = {v: k for k, v in enumerate(A)}
    # dic_B = {v: k for k, v in enumerate(B)}

    res = findSmallestDifference(A, B, m, n)
    print(res)
