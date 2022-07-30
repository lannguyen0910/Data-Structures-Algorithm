from typing import List
from collections import defaultdict


# recusion
def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort()
    leng = len(satisfaction)
    mem = defaultdict(int)

    def calc(i, time, satisfaction):
        if i >= leng:
            return 0
        elif (i, time) in mem:
            return mem[(i, time)]
        else:
            A = calc(i + 1, time + 1, satisfaction) + time*satisfaction[i]
            B = calc(i + 1, time, satisfaction)
            mem[(i, time)] = max(A, B)
            return mem[(i, time)]

    return calc(0, 1, satisfaction)


# DP
def maxSatisfaction2(satisfaction: List[int]) -> int:
    satisfaction.sort()
    length = len(satisfaction)
    dp = [[0 for _ in range(length)] for _ in range(length)]
    for d in range(length):
        dp[0][d] = satisfaction[d]
    for t in range(1, length):
        for d in range(t, length):
            dp[t][d] = dp[t-1][d-1] + satisfaction[d] * (t+1)

    print(max([ele for row in dp for ele in row]+[0]))


print(maxSatisfaction2([-1, -8, 0, 5, -9]))
