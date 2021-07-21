# brute-force: 2d array nxm <=10^6 to generate values. Move to 1d array (nxm) and sort. O(nxm log(nxm))

# We try to binary search (chat nhi phan) the result X and then count how many sums are less than X.
# To count we consider each i, see how many j so that i^2 + j^2 <= X. Do the same for all i's.
# Counting how many j can be done using 2 pointers technique. The complexity is O((n + m) log (n^2 + m^2))

r"""
(binary search) X = 1→ n^2 + m^2:
	j = m
	count = 0
	i = 1 → n:
		while j > 0 and i^2 + j^2 > X:
			j--
		if i^2 <= X:
			count += j

	if count >= k:
		res = X
"""
