# isalnum() - Kiểm tra một chuỗi có phải là số không
myText = "TrongHoa12Tuoi"
print(myText.isalnum()) # output: True
myText = "TrongHoa 12Tuoi"
print(myText.isalnum()) # output: False ( vì có 2 từ trở lên , cách nhau bằng dấu cách thì được gọi là một văn bản)
