thisString = "Hello"
print(type(thisString))
thisString = 'Hello'
print(type(thisString))

print("Toi la mot chuoi do hahaha")
print("Toi cung vay ma nguoi ae")

# cách thông thường
print("Xin chào tớ là Hòa")
print("Tớ năm nay 13 tuổi")
print("Sống tại đâu đó")
# cách ngắn gọn hơn
print("""Xin chào tớ là Hòa
Tớ năm nay 13 tuổi
Sống tại đâu đó""")

myProfile = """Xin chào tớ là Hòa
Tớ năm nay 13 tuổi
Sống tại đâu đó"""
myGF = '''Xin chào tớ là AIDO
Tớ năm nay 99 tuổi
Sống tại đâu đó'''
print(myProfile)

# Dấu nháy kép (") có thể chứa được dấu nháy đơn (')
print("Xin chào my name is 'HoA'")
# Và ngược lại
print('Xin chào my name is "Hoa"')

# Ngoài ra có thể lòng nháy kép vào nháy kép bằng cách
print("Xin chào my name is \"Hoa\"")
# Tương tự vậy với nháy đơn
print('Xin chào my name is \'Hoa\'')

myString = "Hello"
#vi tri:    01234

myString = "Hello"
# output
print(myString[0]) # H 
print(myString[1]) # e 
print(myString[2]) # l 
print(myString[3]) # l 
print(myString[4]) # o
# output
myLocal = myString[0]+myString[1]+myString[2]+myString[3]+myString[4] # Hello
print(myLocal) # Hello 
