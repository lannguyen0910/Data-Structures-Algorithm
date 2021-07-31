import copy


def input():
    with open('./source/Bai20/input.txt', 'r') as f:
        data = f.read()
        lines = data.splitlines()
    arrays = []
    for line in lines[1:]:
        row = line.split(' ')
        x, y = [int(i) for i in row]
        arrays.append((x, y))
    return arrays


def solution1(points):
    """
    Cách này dựa trên giả thiết rằng với mỗi điểm trong mặt phẳng,
    luôn tồn tại một điểm khác sao cho khi nối 2 điểm lại tạo thành
    đường thẳng chia 2 phần có số lượng điểm bằng nhau.

    Chọn một điểm nằm trên bao lồi, với giả thiết ban đầu ta xét điểm 
    này với tất cả các điểm còn lại. Khi này, ta cần sắp xếp tất cả các 
    điểm còn lại theo chiều kim đồng hồ. Và duyệt lần lượt qua chúng.

    Điểm cần tìm sẽ là điểm thứ n/2 trong dãy điểm đã sắp xếp.

    Thuật toán sắp xếp là MergeSort với hàm so sánh dựa vào diện tích đại số

    Space:  O(N*logN)
    Time:   O(N*logN)
    """

    def find_a_point_on_convex(points):
        """
        Lấy điểm trái nhất trên mặt phẳng (điểm này sẽ thuộc bao lồi)
        """
        min_x = int(10e7)
        min_idx = 0
        for idx, point in enumerate(points):
            x, y = point
            if x < min_x:
                min_x = x
                min_idx = idx
        return min_idx

    def sort_point_clockwise(points, base=(0, 0)):
        """
        Dùng diện tích đại số để sắp xếp các điểm theo chiều kim đồng hồ
        """

        def get_area(point1, point2, point3):
            """
            Tính diện tích đại số của tam giác dựa vào 3 điểm
            """
            return (point1[0] - point2[0]) * (point1[1] + point2[1]) + (point2[0] - point3[0]) * (point2[1] + point3[1]) + (point3[0] - point1[0]) * (point3[1] + point1[1])

        def lesser(point1, point2, base=(0, 0)):
            """
            So sánh hai điểm, dựa vào diện tính đại số so với cơ sở base
            """
            S = get_area(point1, base, point2)

            if S < 0:  # Tam giác ngược chiều point1 > point2
                return False
            else:  # Tam giác thuận chiều point1 < point2
                return True

        def merge(arr1, arr2, base=(0, 0)):
            """
            Merge hai mảng đã sort thành một mảng lớn đã sort
            """
            merged = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if lesser(arr1[i], arr2[j], base):
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1

            while i < len(arr1):
                merged.append(arr1[i])
                i += 1

            while j < len(arr2):
                merged.append(arr2[j])
                j += 1

            return merged

        def split(arr, n):
            """
            Chia mảng thành 2 phần
            """
            arr1 = arr[:int(n/2)]
            arr2 = arr[int(n/2):]
            return arr1, arr2

        def sort(array, k, base=(0, 0)):
            """
            Mergesort các điểm dựa trên diện tích đại số
            """
            if k <= 1:
                return array

            arr1, arr2 = split(array, k)
            sorted1 = sort(arr1, len(arr1), base)
            sorted2 = sort(arr2, len(arr2), base)
            merged = merge(sorted1, sorted2, base)

            return merged

        sorted_points = sort(points, len(points), base)
        return sorted_points

    def find_optimal_point(sorted_points, points):
        """
        Tìm điểm thứ 2 thỏa mãn đề, theo giả thuyết thì là điểm 
        ở giữa của mảng các điểm đã sắp xếp theo diện tích hình học
        """
        n = len(sorted_points)
        optimal_point = sorted_points[int(n/2)]
        optimal_point_idx = points.index(optimal_point)
        return optimal_point_idx

    # Chọn một điểm trên bao lồi ==> O(N)
    first_point_idx = find_a_point_on_convex(points)

    # Các điểm còn lại khác điểm đã chọn
    remain_points = points[:first_point_idx]+points[first_point_idx+1:]

    # Sắp xếp các điểm đó theo chiều kim đồng hồ ==> O(N*logN)
    sorted_points = sort_point_clockwise(
        remain_points, points[first_point_idx])

    # Tìm điểm thứ hai thỏa đề ==> O(1)
    second_point_idx = find_optimal_point(sorted_points, points)

    return first_point_idx, second_point_idx  # Total: O(N*logN)


if __name__ == '__main__':
    arrays = input()
    result = solution1(arrays)
    print(result)
