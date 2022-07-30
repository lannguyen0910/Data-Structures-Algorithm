# list all the permutation: O(n!)


def perm(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]


perm([1, 2, 3])

"""
With any permutation, we just need to calculate how many permutations before it. To do this we need to quickly compute the permutation of any n.
Then considering the current digit, if it is greater than 1 then we know that it will undergo at least a pile of permutations with 
the first digit being 1, and this number we know. Similarly if the second digit is greater than "1" (here 1 may not be the smallest number
in the permutation) then we know the same thing. So just consider the digits from 1 → n. The complexity is O(n^2).
"""

# p, flag, a = [], [], []
# p[0] = 1  


# def fromPermutationToOrder(n):
#     res = 0
#     for i in range(1, 21):
#         p[i] = p[i - 1] * i

#     for i in range(n):
#         for k in range(1, a[i]):
#             if not flag[k]:
#                 res += p[n - i - 1]
#         flag[a[i]] = True

#     print(res)


# def fromOrderToPermutation(n):
#     t = a[n]
#     for i in range(n):
#         cnt = 1
#         while t > p[n - i - 1]:
#             t -= p[n - i - 1]
#             cnt += 1
#         for k in range(1, n + 1):
#             if flag[k]:
#                 cnt -= 1
#                 if cnt == 0:
#                     a[i] = k
#                     flag[k] = False
#                     break

#     for i in range(n):
#         print(a[i], end=" ")
