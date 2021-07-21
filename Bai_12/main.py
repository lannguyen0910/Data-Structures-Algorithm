# C1
# The simple way is to calculate each g(i=2 → n).
# To calculate g(i), we iterate p, calculate q = 2i - p, check for primes.
# Time complexity is O(n^2 * root(n))

# C2
# We see that instead of calculating g(i) in the above way, we only need to check which pair p, q
# belongs to g(i). This happens because a pair p, q belongs to exactly one g(i).
# So we only need to count the number of pairs p, q such that p + q <= 2n.
# It is easy to see that we can list the primes < n for easy calculation.
# The sieve can be used for enumeration. After the enum is complete, use 2 pointers to calculate the number of
# possible p, q pairs. Time complexity is O(n) and the space complexity is also O(n) due to using sieve.


# we can drop sieve for enumeration if we use quick prime number checking algorithms or something.
# The complexity is O(nk) with k depending on the algorithm used (k <= root n)
def sieve(n):

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False


# pseudo
p = sieve(n)
j = m
for i in range(1, m):
    if i <= j:
        while p[i] + p[j] > 2*n:
            j -= 1
        res += j - i + 1
    else:
        break
