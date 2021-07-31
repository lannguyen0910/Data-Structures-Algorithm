def input():
    with open('./source/Bai16/input.txt', 'r') as f:
        data = f.read()
        lines = data.splitlines()
    n = int(lines[0])

    array1 = [int(i) for i in lines[1].split(' ')]
    array2 = [int(i) for i in lines[2].split(' ')]

    return array1, array2


def lesser(pair1, pair2):
    """
    So sánh hai cặp nối
    """
    return pair1[0] < pair2[0] and pair1[1] < pair2[1]


def solution1(array1, array2):
    """
    Thuật toán ngây thơ, tìm dãy con tăng dài nhất
    Sinh ra tất cả cặp nối có thể (i,j) sao cho a[i] = b[j],

    Với mỗi bộ (i,j), xét tất cả dãy (i,j); (i+k,j+p);,... 
    (k,p>0) để tìm dãy con tăng dài nhất

    Ta có thể sử dụng quy hoạch động để tìm dãy con tăng dài nhất
    Thực hiện cách tìm dãy con tăng dài nhất truyền thống, thực
    hiện thuật toán này trong O(N^2)

    dp[i] lưu độ dài dãy tăng dài nhất đến bao gồm vị trí i.

    Space:  O(N) ==> Sinh ra các cặp
    Time:   O(N^2)
    """

    # Tìm tất cả cặp nối, các cặp sau khi tìm sẽ được sắp xếp thứ tự theo phần tử đầu tiên
    pairs = []
    for i, ai in enumerate(array1):
        for j, aj in enumerate(array2):
            if ai == aj:
                pairs.append((i, j))
                break

    # Mảng dp[i] lưu độ dài dãy tăng dài nhất đến vị trí i
    n = len(array1)
    dp = [1 for i in range(n)]

    for i in range(1, n):                # O(N)
        for j in range(i):              # O(N)
            if lesser(pairs[j], pairs[i]):
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)  # Total: O(N^2)


if __name__ == '__main__':
    array1, array2 = input()
    result = solution1(array1, array2)
    print(result)
