"""
Ta nhận xét rằng, 1 cụm chỉ có thể có 3 khả năng là thuộc nhóm 1, thuộc nhóm 2 hoặc không thuộc nhóm nào. 
Từ đó dẫn đến ta chạy hết tất cả mọi trạng thái có thể của các cụm này và tính kết quả lớn nhất. Độ phức tạp O(3^k)
"""


"""
Ta sort giảm dần các cụm theo nhóm 1. Khi đó giả sử ta chọn n + m cụm đầu và đều lấy giá trị của nhóm 1, 
và sẽ dư ra k - (n + m) cụm chưa chọn thì ta cho giá trị của nhóm 1 của các cụm ấy bằng 0.

Lúc này ta chỉ cần chọn ra m cụm cho nhóm 2 là được. Nhưng chọn thế nào cho tối ưu?
 Ta thấy nếu một cụm đang nhóm 1 mà bị đem sang nhóm 2 thì giá trị của nó mang lại cho kết quả sẽ là b - a. 
 Do đó ta chỉ cần tính giá trị b - a cho k cụm rồi sort lại theo giảm dần, chọn ra m cụm theo thứ tự đó là được. 
 Lưu ý là lúc chọn n + m cụm đầu thì có vài cụm dư ra, nếu trong quá trình chọn m cụm sau 
 mà lọt vào đám này thì nên cẩn thận tính lại số lượng.
"""

r"""
sort1
i = 1 → n+m:
	res += ai
i = n + m + 1 → k
	ai = 0
i = 1 → k:
	bi -= ai
    
sort2
i = 1 → m:

"""
