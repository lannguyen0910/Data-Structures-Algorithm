# https://www.geeksforgeeks.org/area-of-a-polygon-with-given-n-ordered-vertices/
# Công thức tính diện tích đa giác là:
# | 1/2 [ (x1y2 + x2y3 + … + xn-1yn + xny1) – (x2y1 + x3y2 + … + xnyn-1 + x1yn) ] |

# Có thể thấy diện tích trên cũng được xem là tổng cộng dồn các diện tích lại với nhau.
# Vậy ta có thể tính trước diện tích đa giác từ đỉnh 1 đến đỉnh i để tiện cho việc
# tính diện tích của đa giác con tạo bởi các cạnh liên tiếp nhau.

# Đó là các nhận xét cơ bản đầu tiên. Có thể thấy để chia đa giác ra thành 2 nửa 
# thì ta cần 2 đỉnh trong đa giác, vẽ một đoạn thẳng nối 2 điểm lại với nhau là được. 
# Sau khi có 2 hình đa giác con thì dùng cách trên để tính diện tích một cách nhanh chóng. 
# Độ phức tạp cuối cùng là O(n^2) để tìm 2 điểm bất kì.


# (X[i], Y[i]) are coordinates of i'th point.
def polygonArea(X, Y, n):

    # Initialize area
    area = 0.0

    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0, n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i   # j is previous vertex to i

    # Return absolute value
    return int(abs(area / 2.0))


# Driver program to test above function
X = [0, 2, 4]
Y = [1, 3, 7]
n = len(X)
print(polygonArea(X, Y, n))


# Cải tiến: Giả sử ta đã có sẵn 2 đỉnh bất kỳ nào đó trong đa giác. 
# Đầu tiên ta thử cố định đỉnh thứ nhất, đỉnh thứ 2 ta sẽ cho nó di chuyển.
#  Có thể thấy rằng diện tích của đa giác 1 sẽ dần lớn ra và diện tích đa giác 2 dần nhỏ đi, 
# đồng nghĩa khoảng cách giữa chúng sẽ nhỏ lại. Nếu đến một lúc nào đó mà khoảng cách này 
# lại lớn lên trở lại thì có thể thấy việc tiếp tục di chuyển đỉnh 2 sẽ trở nên vô nghĩa.
#  Khi đó ta bắt đầu dịch đỉnh 1 lên một bước và lặp lại các bước như trên.
#  Cuối cùng ta sẽ được kết quả mong muốn. Kỹ thuật này được biết đến là 2 con trỏ.
#  Độ phức tạp cuối cùng là O(n).

# u = 1, v = 2
# while u <= n
# while (true)
# 		V = (v + 1) % n + 1
# 		if D(u, v) < D(u, V) break
# 		v++
# 	res = min(D(u, v))
# 	u++
u = 1
v = 2
while u <= n:
    while(True):
        V = (v + 1) % n + 1
        if diff(u, v) < diff(u, V): # Chênh lệch diện tích của 2 đa giác cắt bởi đoạn thẳng uv / uV
            break
        v += 1
    res = min(res, diff(u, v))
    u += 1