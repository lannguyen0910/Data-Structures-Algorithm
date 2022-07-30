class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first = 1
        second = 1

        for i in range(2, n+1):
            steps = first + second
            first = second
            second = steps

        return steps


class Solution(object):
    a = {1: 1, 2: 2}

    def climbStairs(self, n):
        for i in range(3, n + 1):
            self.a[i] = self.a[i - 1] + self.a[i - 2]
        return self.a[n]


n = 10
test = Solution()
test.climbStairs(n)
