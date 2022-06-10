# find() + index() - Tìm kiếm một kí tự trong chuỗi

#-- find sẽ trả về vị trí mà nó tìm được, và trả về -1 nếu không tìm thấy
#-- index cũng có chức năng tương tự find, nhưng sẽ lỗi nếu không tìm thấy
myText = "Trong hoa"
print(myText.find("Trong")) # output: 0
print(myText.index("Trong")) # output: 0

myText = "TrongHoa dep trai nhi?"
         #0123456789012345678901
print(myText.find("H",4,6)) # Tìm H từ vị trí 4 tới 6 [ kết quả H nằm ở vị trí 5 ]
print(myText.index("H",4,6)) # index cũng tương tự find

#Trả lỗi
print(myText.find("A")) # output: -1
print(myText.index("A")) # Báo lỗi

