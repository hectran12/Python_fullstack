import os, time
con_cho = {}
exp = 0

def Menu():
    lMenu = ['Nhân nuôi','Nuôi chó']
    for x in range(len(lMenu)):
        print('[',x+1,'] ',lMenu[x])

def taoconcho():
    namedog = input('Nhập tên cho con chó: ')
    con_cho['name'] = namedog
    print('Nhận nuôi thành công!')
    return 0

def getinfo_dog():
    print('Exp: ',exp,' || Level: ' ,round(exp/1000))

def nhannuoi():
    try:
        print('Bạn chấp nhận bỏ con chó ',con_cho['name'], ' (y/): ')
        ask = input()

        if ask.lower() == 'y':
            taoconcho()
        else:
            print('Vậy không nhận nuôi nữa!')
    except:
        taoconcho()
    
    return 0

def MenuNuoi():
    lMenuNuoi = ['Cho ăn','Chơi cùng','Tắm rửa']
    for x in range(len(lMenuNuoi)):
        print('[',x+1,'] ',lMenuNuoi[x])

def An():
    dictMenu = {
        'Thịt Gà' : 200,
        'Thịt Bò' : 300,
        'Cua Hoàng Đế' : 400
    }

    i = 0
    for x , y in dictMenu.items():
        print('Nhập ',i+1,' cho ăn ',x,' [nhận được ',y,']')
        i = i + 1

    askMonAn = int(input('Nhập số muốn cho ăn: '))
    if askMonAn == 1:
        expCong = 200
    elif askMonAn == 2:
        expCong = 300
    elif askMonAn == 3:
        expCong = 400
    else:
        print('Đừng cho chó bạn ăn không khí chứ')
        expCong = 0
    
    print('Cho bạn đã tăng ',expCong,'exp!')
    return expCong

def ChoiCung():
    for x in range(40):
        print('Bạn đang vui chơi với chó trong ',40-x,' gây!    ',end='\r')
        time.sleep(1)

    print('Chơi rất vui , chó của bạn đã tăng được 100exp')
    
    return 100

def TamCho():
    options = {
        'Dùng xà phòng' : 2,
        'Không dùng xà phòng' : 1
    }

    i = 0
    for x , y in options.items():
        print('Nhập ',i+1,' để ',x,' tăng thêm ',y,' exp')
        i += 1
    
    askTamOpt = int(input('Nhập số: '))
    if askTamOpt == 1:
        expCong = 2
    elif askTamOpt == 2:
        expCong = 1
    else:
        expCong = 0
    
    for x in range(40):
        print('Đang tắm cho chó , bạn vui lòng đợi ',40-x,' giây!',end='\r')
        time.sleep(1)

    print('Thành công cộng ',200+expCong,'exp cho chó của bạn')

    return 200 + expCong

def nuoicho():
    MenuNuoi()
    ask = int(input('Nhập số: '))

    if ask == 1:
        expR = An()
    elif ask == 2:
        expR = ChoiCung()
    elif ask == 3:
        expR = TamCho()
    else:
        print('Không có mục này trong menu')

    return expR


    
while True:
    os.system('cls')
    check_ex_dogs = False
    try:
       print('Thông tin chú cún ',con_cho['name'])
       getinfo_dog()
       check_ex_dogs = True
    except:
        print('Bạn chưa có con chó nào đang nhận nuôi')
    Menu()
    chucnang = int(input('Nhập số: '))

    os.system('cls')
    if chucnang == 1:
        exp += nhannuoi()
    elif chucnang == 2:
        
        if check_ex_dogs:
            exp += nuoicho()
        else:
            print('Vui lòng nhận nuôi một con chó , để sử dụng chức năng này!!')

    else:
        print('Chọn lại đi')
    input('Enter để quay lại menu')
