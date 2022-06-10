# count() - Đếm số lần xuất hiện trong chuỗi
myString = "Cuốn truyện này thật haha và buồn cười haha haha haha haha :("
#                                1                 2    3    4    5
#           0123456789012345678901234567890123456789012345678901234567890
print(myString.count("haha")) # có 5 haha tổng tất cả
print(myString.count("haha",20,30)) # Kiểm tra từ vị trí 20 tới 30 và có 1 haha
