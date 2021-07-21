"""
Nhận xét được rằng dù thực hiện các thao tác theo bất kỳ thứ tự nào đều cũng cho ra số duy nhất 
do tính chất đồng dư của phép cộng.

Ta biết rằng để biến dãy n phần tử còn lại 1 phần tử thì bước kế cuối phải có đúng 2 phần tử.
Nếu suy ngược lại, 2 phần tử này cũng là kết quả của hai dãy liên tiếp, và chắc chắn tổng số phần tử của hai dãy 
bằng n. Do đó ta nghĩ đến thuật chia để trị.

Đầu tiên ta tính chi phí cho các dãy có độ dài là 2→ k - 1 trước. Sau đó các dãy độ dài k sẽ được tính lại 
từ các cặp dãy con của dãy này. Do đó dẫn đến đây là quy hoạch động.
Độ phức tạp sẽ là O(n^3)
"""

r"""
len = 2 → n:
	i = 1 → n - len + 1:
		j = i + len - 1
		k = i → j - 1:
			dp[i][j] = min(dp[i][k] + dp[k + 1][j] + cost([i..k], [k + 1..j]))
dp[1][n] = res

"""
