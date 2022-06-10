# expandtabs() - Tăng kích thước cách của \t 
print("Trong hoa\tneeeeee!".expandtabs(1)) # output: Trong hoa neeeeee!
# Gia hạn khoảng cách nhiều cho \t
print("Trong hoa{0} , ne ma {1} huhuu".format("\t".expandtabs(10),"\t".expandtabs(10))) # output: Trong hoa           , ne ma            huhuu
tabH = "\t".expandtabs(10) 
print("Trong hoa"+tabH+"ne"+tabH+"haha") # output: Trong hoa          ne          haha
