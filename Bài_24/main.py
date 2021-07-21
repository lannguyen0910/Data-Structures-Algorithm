# Since each digit of m has only two possibilities of 0 or 1, the number of possible numbers m can be 2k
# where k is the number of digits of m. From here we just need to traverse all m using bitwise processing
# to find the result. O(2^k*k*P) complexity where P is the complexity of division and remainder.


# Pseudo
# i = 0 → 2k - 1: (i is in binary form)
# 	m = 0
# 	j = k - 1 → 0:
# 		m = m * 10 + ((i & (1 << j)) == 1 ? 1: 0)
# 	m % n == 0 ? break: next
