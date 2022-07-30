
# brr=[(1,1),(2,2),(3,0)]
arr = [5, 4, 3, 1, 2, 6]
n = 6
brr = {arr[k]: k for k in range(n)}


# This greedy approach doesn't guarantee the MINIMUM flips
# Time: O(n*n)
# Space: O(n)

def minFlips1(n, arr):
    count = 0
    temp = []
    target = [i + 1 for i in range(len(arr))]
    for i in range(n):
        # DP steps
        if arr[i] != i+1:
            # arr[index] = i-1
            index = brr[i+1]
            # reverse that portion
            # reverse O(n), concate O(n)
            temp = arr[index+1:]
            arr = arr[:i]+list(reversed(arr[i:(index+1)]))

            if index + 1 < n:
                arr = arr + temp
            count += 1

            if arr == target:
                print(count)
                return count

    return -1


# print(minFlips1(n, arr))


# BFS: Worst case O(n!)
# We consider each possible state of a permutation to be a node on the graph.
# It can be observed that if through an inversion, one state can be changed to another,
# then we have an edge connecting these two nodes. Then we just need to start from the initial state,
# use n inversions to find the next n states, mark again and repeat the above until we get the best result.
# The above browsing is based on BFS to ensure accurate results.

# Ta xem mỗi trạng thái có thể có của một hoán vị là một nút trên đồ thị.
# Quan sát được nếu qua một phép đảo mà từ trạng thái này có thể sang trạng thái khác thì
# ta có một cạnh nối giữa hai nút này. Khi đó ta chỉ cần bắt đầu từ trạng thái ban đầu,
# sử dụng n phép đảo ngược để tìm ra n trạng thái tiếp theo, đánh dấu lại và lặp lại việc trên
# cho đến khi ra được kết quả tốt nhất. Quá trình duyệt trên được dựa trên BFS để đảm bảo ra kết quả chính xác
# Độ phức tạp của cách làm này sẽ là O(n!) trong trường hợp xấu nhất, nhưng với kết quả nhỏ thì
# độ phức tạp sẽ giảm đi đáng kể.
# Có thể thấy với cách thứ hai có thể đảm bảo kết quả chính xác nhất nhưng lại không hiệu quả về mặt thời gian
# và bộ nhớ. Do đó với cách làm 1 dù kết quả không tốt nhưng vẫn đủ chấp nhận được
# và độ phức tạp có thể cải tiến hơn được nữa nên trên thực tế thì nên sử dụng cách này hay hơn.

def minFlips2(arr):
    n = len(arr)
    seen = set(tuple(arr))
    target = [i + 1 for i in range(len(arr))]
    q = [(arr, 0)]
    while q:
        perm, dist = q.pop(0)
        if perm == target:
            return dist
        for i in range(n+1):
            for j in range(i + 2, n+1):
                child = perm[:i] + list(reversed(perm[i:j])) + perm[j:]
                if tuple(child) not in seen:
                    seen.add(tuple(child))
                    q.append((child, dist + 1))
    return -1


print(minFlips2(arr))
