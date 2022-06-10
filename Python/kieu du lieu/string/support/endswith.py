# endswith() - Kiểm một chuỗi có kết thúc bằng kí tự
myText = "Hello xin chào mình tên là Trong Hoa"
         #012345678901234567890123456789012345
print(myText.endswith("Hoa")) # output: True , tức là có kết thúc bằng "Hoa"
print(myText.endswith("xin",4,9)) # output: True , vì từ vị trí tới 4 và 9 có kết thúc bằng "xin"
