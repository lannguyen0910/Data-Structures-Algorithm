class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n

    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)
            print("update i: ", i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        print("query res: ", i)
        return res


def reversePairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # BIT O(nlogn)
    new_nums = nums + [x for x in nums]
    print(new_nums)
    sorted_set = sorted(list(set(new_nums)))
    print(sorted_set)
    tree = BIT(len(sorted_set))
    res = 0
    ranks = {}
    for i, n in enumerate(sorted_set):
        ranks[n] = i + 1
    print('Ranks: ', ranks)
    print(' nums[::-1]: ',  nums[::-1])
    for n in nums[::-1]:
        res += tree.query(ranks[n] - 1)
        print('res: ', res)
        tree.update(ranks[n], 1)

    return res


print(reversePairs([1, 2, 4, 3, 5, 1]))
