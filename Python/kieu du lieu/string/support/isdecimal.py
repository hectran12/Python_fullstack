# isdecimal() - kiểm tra một chuỗi có phải là số thập phân không
myUnicode = "\u0033" # số 3
print(myUnicode.isdecimal()) # output: True ( vì là số 3 ) 
myUnicode = "\u0047" # chữ G 
print(myUnicode.isdecimal()) # output: False ( vì là chữ G 
