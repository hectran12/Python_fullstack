# isalpha() - Kiểm tra một chuỗi còn toàn là chữ cái không
myText = "Trong Hoa"
print(myText.isalpha()) #output: False
print(myText.replace(" ","").isalpha()) #output: True ( vì TrongHoa là một chữ cái , còn Trong Hoa là hai chữ cái )
