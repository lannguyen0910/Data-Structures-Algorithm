"""
Cách làm cơ bản là phủ n đoạn lên [L, R]. Sau đó thử từng đoạn, nếu bỏ đoạn đó mà trên [L, R] 
có một thằng 0 nghĩa là đoạn đó không bỏ được. Độ phức tạp là O(n(R-L+1))

Vì thấy R-L+1 quá xấu nên ta có thể rời rạc hóa dữ liệu lại để biến nó thành n.

Có thể thấy ta có thể dùng IT, BIT để phủ nhanh trong log n, và cũng dùng nó để kiểm tra nhanh trong log n. 
Tóm lại ta cần IT, BIT min để xây dựng. Độ phức tạp O(n log n)

Tuy nhiên vì ta không có truy vấn gì tùm lum gì cả nên ta có thể sử dụng kỹ thuật phủ nhanh hơn là lùa. 
ới mỗi x, y thì ta đặt a[x] += 1 và a[y + 1] -= 1. Sau đó ta chạy qua một lần để tính prefix sum. 
Mảng a cuối cùng sẽ giống như khi ta dùng IT, BIT. Độ phức tạp O(n)

Đề kiểm tra nhanh thì ta có thể tận dụng mảng a trên. Đầu tiên xóa hết các phần tử lớn hơn 1, 
sau đó tính lại prefix sum một lần nữa. Khi đó nếu trên đoạn có một thằng nào đó bằng 1 thì tổng của đoạn đó 
sẽ lớn hơn 0. Độ phức tạp O(n)

Tổng lại độ phức tạp là O(n log n) do thằng sort để rời rạc hóa là chính.
"""
r"""
i = 1 → n:
    a[xi] +=1
    a[yi + 1] -= 1

i = L → R:
	a[i] += a[i - 1]

i = L → R:
	if a[i] > 1:
		a[i] = 0

i = L → R:
	a[i] += a[i - 1]

i = 1 → n:
	if a[yi] - a[xi - 1] > 0:
		false
	else
		res = maxlen(i)
"""
