import math

# function to find GCD of sub sequence
# of size k with max GCD in the array


def findMaxGCD(arr, n, k):

    # Computing highest element
    high = max(arr)
    print("Highest: ", high)
    # Array to store the count of
    # divisors i.e. Potential GCDs
    divisors = [0] * (high + 1)
    print("divisors: ", divisors)

    # Iterating over every element
    for i in range(n):

        # Calculating all the divisors
        for j in range(1, int(math.sqrt(arr[i])) + 1):

            # Divisor found
            if (arr[i] % j == 0):

                # Incrementing count for divisor
                divisors[j] += 1

                # Element/divisor is also a divisor
                # Checking if both divisors are
                # not same
                if (j != arr[i] // j):
                    divisors[arr[i] // j] += 1
    print("divisors after: ", divisors)
    # Checking the highest potential GCD
    for i in range(high, 0, -1):
        print("i: ", i)
        # If this divisor can divide at least k
        # numbers, it is a GCD of at least one
        # sub sequence of size k
        if (divisors[i] >= k):
            return i


# Driver code
if __name__ == "__main__":

    # Array in which sub sequence with size
    # k with max GCD is to be found
    arr = [2, 6, 4, 3, 18, 12, 24, 8, 7, 5]
    k = 3

    n = len(arr)
    print(findMaxGCD(arr, n, k))
