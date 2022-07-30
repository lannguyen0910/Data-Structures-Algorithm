def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0

    # A loop to slide pat[] one by one
    for i in range(N - M + 1):

        # For current index i, check
        # for pattern match
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            res += 1
            j = 0
    return res


# Driver Code
if __name__ == '__main__':
    txt = "dhimanman"
    pat = "man"
    print(countFreq(pat, txt))
# Time Complexity: O(M * N)


def KMPSearch(pat, txt):

    M = len(pat)
    N = len(txt)

    # Create lps[] that will hold the longest
    # prefix suffix values for pattern
    lps = [None] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[]
    # array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    res = 0
    next_i = 0

    while (i < N):
        if pat[j] == txt[i]:
            j = j + 1
            i = i + 1
        if j == M:

            # When we find pattern first time,
            # we iterate again to check if there
            # exists more pattern
            j = lps[j - 1]
            res = res + 1

            # We start i to check for more than once
            # appearance of pattern, we will reset i
            # to previous start+1
            if lps[j] != 0:
                next_i = next_i + 1
                i = next_i
                j = 0

        # Mismatch after j matches
        elif ((i < N) and (pat[j] != txt[i])):

            # Do not match lps[0..lps[j-1]]
            # characters, they will match anyway
            if (j != 0):
                j = lps[j - 1]
            else:
                i = i + 1

    return res


def computeLPSArray(pat, M, lps):

    # Length of the previous longest
    # prefix suffix
    len = 0
    i = 1
    lps[0] = 0  # lps[0] is always 0

    # The loop calculates lps[i] for
    # i = 1 to M-1
    while (i < M):
        if pat[i] == pat[len]:
            len = len + 1
            lps[i] = len
            i = i + 1

        else:  # (pat[i] != pat[len])

            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment
                # i here

            else:  # if (len == 0)
                lps[i] = len
                i = i + 1


# Driver code
if __name__ == "__main__":

    txt = "geeksforgeeks"
    pat = "eeks"
    ans = KMPSearch(pat, txt)

    print(ans)
# O(M+N)
