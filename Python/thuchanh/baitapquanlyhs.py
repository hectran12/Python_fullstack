# Yêu cầu
"""
- Có menu để người dùng thao tác
ví dụ:
[1] Thêm học sinh
[2] Quản lý ( có xóa/sửa )
Nhập vào số:

[ở chức năng 1]
- Yêu cầu sử dụng từ điển để làm điều này ( gồm mã hs , tên hs , điểm toán , văn , hóa )
[ở chức năng 2]
- Hiển thị tất cả học sinh , có chỗ cho xóa sửa ví dụ 
====================================================
[1] Mã : 123 || Tên : Trọng Hòa || Toán : 9 || Văn : 9 || Hóa : 9
====================================================
Nhập [1+' '+mã hs] để xóa , nhập [2+' '+mã hs] để sửa
====================================================
Mời bạn nhập:
"""

import os , time # sử dụng thư viện os ( để sài os.system('cls') ) và thư viện time để delay
# Hiện menu
def Menu():
    listMenu = ['Thêm học sinh','Quản lý ( xóa / sửa )']
    for i in range(len(listMenu)):
        print('[',i+1,'] ',listMenu[i])
        
dsHS = {}

# Thêm học sinh vào "dsHS"
def ThemHs():

    """
    1. Mã học sinh phải kiểu dữ liệu integer ( int )
    2. Tên học sinh phải kiểu dữ liệu string ( str )
    3. Đối với điểm , do điểm có thể là 0,5 hoặc 9,5 nên phải kiểu dữ liệu float
    """

    MaHs  = int(input('Nhập mã học sinh: '))
    TenHs = input('Tên học sinh: ')
    Toan  = float(input('Điểm Toán: '))
    Van   = float(input('Điểm Văn: '))
    Hoa   = float(input('Điểm Hóa: '))

    # Thêm học sinh vào danh sách
    """
    Tạo một từ điển cơ bản chứa thông tin học sinh
    """

    HocSinh = {
        "tenHS" : TenHs,
        "Toan"  : Toan,
        "Van" : Van,
        "Hoa" : Hoa
    }

    # Đưa vào danh sách
    dsHS[MaHs] = HocSinh

    print('Thêm thành công học sinh vào danh sách!')


# Quản lý học sinh
def QuanLy():
    
    # Kiểm tra số học sinh có trong danh sách

    if len(dsHS) > 0:
        
        while True:
            os.system('cls')
            # Xuất tất cả học sinh trong danh sách
            print('='*30)
            i = 0
            for x , y in dsHS.items():
                i += 1
                print('[',i,'] Mã: ',x,' || Tên: ',y['tenHS'],' || Toán: ',y['Toan'],' || Văn: ',y['Van'],' || Hóa: ',y['Hoa'])
            print('='*30)
            # Hiện menu chỉnh sửa , yêu cầu người dùng chọn
            print('Nhập [1+\' \'+mã hs] để xóa , nhập [2+\' \'+mã hs] để sửa')
            print('='*30)
            nhap = input('Mời bạn nhập: ')

            # xử lý nhập
            """
            Qúa trình xử lý:
            - Tách ' ' trong chuỗi người dùng vừa nhập
            - Lấy [0] trong tách làm chỉ định chức năng
            - Lấy [1] trong tách làm mahs yêu cầu
            - Sử dụng câu lệnh điều kiện để so sánh ( lưu ý tách ra thì là string )
            """
            tach = nhap.split(' ')
            chucnang = tach[0]
            if len(tach) > 1:
                maHs = int(tach[1])

            if chucnang == '1':
                del dsHS[maHs]
                print('Xóa thành công!')
                time.sleep(1)

            elif chucnang == '2':
                TenHs = input('Tên học sinh: ')
                Toan  = float(input('Điểm Toán: '))
                Van   = float(input('Điểm Văn: '))
                Hoa   = float(input('Điểm Hóa: '))
                HocSinh = {
                    "tenHS" : TenHs,
                    "Toan"  : Toan,
                    "Van" : Van,
                    "Hoa" : Hoa
                }
                dsHS[maHs] = HocSinh
                print('Chỉnh sửa thành công')
                time.sleep(1)

            else:
                print('Đã thoát khỏi quản lý')
                break
        
    else:
        print('Không có học sinh!') # nếu số học sinh trong danh sách lớn hơn 0 thì sẽ xem được quản lý


while True:
    os.system('cls')
    # gọi menu và yêu cầu người dùng chọn chức năng
    Menu()
    chon = int(input('Nhập vào số: '))
    if chon == 1:
        ThemHs()
    elif chon == 2:
        QuanLy()
    else:
        print('Bạn chọn không đúng')
    
    input('Enter để tiếp tục')
