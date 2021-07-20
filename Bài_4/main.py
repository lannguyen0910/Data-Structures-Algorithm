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


print(reversePairs([5, 2, 6, 1]))


def countSmaller(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # merge sort result -
    # sorted array in tuples [ (val1, idx1), (val2, idx2) and so on ]
    # Count array to hold count of inversion of every index

    # 1. create a tmp array holding - [(val, idx), (val2, idx2)]
    # 2. run merge sort on tmp array
    # 3. merge condition:
    # i1 index iterates over left array, i2 iterates over right array
    # if left[i1] > right[i2]:
    # - that means all elements in left after this left element needs atleast 1 increase in
    # inversion because
    # all of them are greater than right[i2]
    # - thats why keep a count of inversions variable. for every inversion needed,
    # increase inversions var

    self.counts = [0]*len(nums)

    def merge(left, right):
        i1, i2 = 0, 0
        inversions = 0
        arr = []
        if not left:
            return right
        if not right:
            return left

        # to hold a list of i1 indexes for which self.count[i1] has received inversions.
        set1 = set()
        while i1 < len(left) or i2 < len(right):
            if i2 >= len(right):
                if left[i1][1] not in set1:
                    set1.add(left[i1][1])
                    self.counts[left[i1][1]] += inversions
                arr.append(left[i1])
                i1 += 1
                continue

            if i1 >= len(left):
                arr.append(right[i2])
                i2 += 1
                continue

            if left[i1][0] > right[i2][0]:
                inversions += 1
                if left[i1][1] not in set1:
                    # first left[i1] > right[i2] gets all inversions in count.
                    set1.add(left[i1][1])
                    self.counts[left[i1][1]] += inversions
                else:
                    # consecutive invesions adds 1
                    self.counts[left[i1][1]] += 1
                arr.append(right[i2])
                i2 += 1
            else:
                if left[i1][1] not in set1:
                    set1.add(left[i1][1])
                    self.counts[left[i1][1]] += inversions
                arr.append(left[i1])
                i1 += 1

        # print("count: {}".format(self.counts))
        return arr

    def mergesort(arr):
        if len(arr) <= 1:
            return arr

        if arr:
            mid = len(arr) / 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            res = merge(left, right)
            return res

    tmp_array = []
    for i, val in enumerate(nums):
        tmp_array.append((val, i))

    mergesort(tmp_array)
    return self.counts

#   time - O(n) + O(nlogn) = O(nlogn)
# 	 space - O(n)
