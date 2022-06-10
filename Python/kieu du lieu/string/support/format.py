myName = "Trong Hoa"
myAge = 19
myLocation = "Ba Ria"
myString = "Xin chào tôi tên là {0}, hiện tại đạng {1} và sống ở {2}".format(myName,myAge,myLocation)
print(myString) # output: Xin chào tôi tên là Trong Hoa, hiện tại đạng 19 và sống ở Ba Ria

myName = "Trong Hoa"
myAge = 19
myLocation = "Ba Ria"
myString = "Bạn tôi sống ở {2}, hiện nay anh ấy {0} tuổi và tên là {1}".format(myAge,myName,myLocation)
#myAge = 0 , myName = 1 , myLocation = 2
print(myString)

myName = "Trong Hoa"
myAge = 19
myLocation = "Ba Ria"
myString = "Tôi tên là {} hiện nay {} và sống ở {}".format(myName,myAge,myLocation)
# myName = 0 , myAge = 1 , myLocation = 2
print(myString) # Tôi tên là Trong Hoa hiện nay 19 và sống ở Ba Ria
