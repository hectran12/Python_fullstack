# encode() - Encode string
myText = "Trọng Hòa đẹp trai"
Encode_normal = myText.encode() # Encode sang mã utf-8
print(Encode_normal); # output: b'Tr\xe1\xbb\x8dng H\xc3\xb2a \xc4\x91\xe1\xba\xb9p trai'

#cú pháp cụ thể: {string}.encode(encoding={encoding}, errors={errors})

#sử dụng dấu gạch chéo ngược thay vì ký tự không thể mã hóa 
Encode_backslashreplace = myText.encode(encoding="ascii",errors="backslashreplace") # output: b'Tr\\u1ecdng H\\xf2a \\u0111\\u1eb9p trai'
print(Encode_backslashreplace) 
#Bỏ quá các kí tự không thể mã hóa
Encode_ignore = myText.encode(encoding="ascii",errors="ignore") # output: b'Trng Ha p trai'
print(Encode_ignore)
#Encode và giải thích lý do Encode
Encode_namereplace = myText.encode(encoding="ascii",errors="namereplace") # output: b'Tr\\N{LATIN SMALL LETTER O WITH DOT BELOW}ng H\\N{LATIN SMALL LETTER O WITH GRAVE}a \\N{LATIN SMALL LETTER D WITH STROKE}\\N{LATIN SMALL LETTER E WITH DOT BELOW}p trai'
print(Encode_namereplace)
#Thay thế những kí tự chuyển đổi và thay thế thành dấu chấm hỏi
Encode_replace = myText.encode(encoding="ascii",errors="replace") # output: b'Tr?ng H?a ??p trai'
print(Encode_replace)
#Thay thế thành mã xml
Encode_xmlcharrefreplace = myText.encode(encoding="ascii",errors="xmlcharrefreplace") # output: b'Tr&#7885;ng H&#242;a &#273;&#7865;p trai'
print(Encode_xmlcharrefreplace)
#Phát sinh lỗi khi encode không thành công
Encode_strict = myText.encode(encoding="ascii",errors="strict")
print(Encode_strict)
