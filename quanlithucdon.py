from quanliquan import QuanLiQuan
class QuanLiThucDon:
    lThucPham = []
    lThucAn = []
    lThucUong = []

    @staticmethod
    def ThemThucAn():
        from thucan import ThucAn
        ta = ThucAn()
        ta.TaoThucAn()
    
    @staticmethod
    def ThemThucUong():
        from thucuong import ThucUong
        tu = ThucUong()
        tu.TaoThucUong()
    
    @staticmethod
    def XoaThucAn():
        TenThucAn = input("Ten Thuc An Muon Xoa: ")
        ta = next((x for x in QuanLiThucDon.lThucAn if x.Ten == TenThucAn), None)
        if ta != None:
            QuanLiThucDon.lThucPham.remove(ta)
            QuanLiThucDon.lThucAn.remove(ta)
        else:
            print("Khong Tim Thay")

    @staticmethod
    def XoaThucUong():
        TenThucUong = input("Ten Thuc Uong Muon Xoa: ")
        tu = next((x for x in QuanLiThucDon.lThucUong if x.Ten == TenThucUong), None)
        if tu != None:
            QuanLiThucDon.lThucPham.remove(tu)
            QuanLiThucDon.lThucUong.remove(tu)
        else:
            print("Khong Tim Thay")

    @staticmethod
    def HienThi(ds):
        print("\t\t\t ------------------------------------------------------------------------------")
        print("\t\t\t Ten Mon             | Gia      | Tinh Trang | Thoi Diem Ban            | Loai")
        print("\t\t\t ------------------------------------------------------------------------------")
        for x in ds:
            x.HienThi()
        print("\t\t\t ------------------------------------------------------------------------------\n")
    @staticmethod
    def ThucDon():
        print("\t\t\t -----------------------------------THUC DON-----------------------------------\n")
        print("\t\t\t | Thuc An |")
        QuanLiThucDon.HienThi(QuanLiThucDon.lThucAn)
        print("\t\t\t | Thuc Uong |")
        QuanLiThucDon.HienThi(QuanLiThucDon.lThucUong)


    @staticmethod
    def SapXep(flag, ds):
        if flag == 1:
            temp = sorted(ds, key=lambda x: x.Gia)
        elif flag == 2:
            temp = sorted(ds, key=lambda x: x.Gia, reverse=True)
        return temp
    
    @staticmethod
    def TimKiemTheoKhoangGia(Gia1, Gia2, ds):
        return [x for x in ds if x.Gia >= Gia1 and x.Gia <= Gia2]

    @staticmethod
    def MenuQuanLiThucDon():
        chon = None
        while True:
            print("\t\t\t |==============================Quan Li Thuc Don===============================|\n")
            print("\t\t\t |                            0. Quay Lai                                      |\n")
            print("\t\t\t |                            1. Thuc Don                                      |\n")
            print("\t\t\t |                            2. Them Mon                                      |\n")
            print("\t\t\t |                            3. Xoa Mon                                       |\n")
            print("\t\t\t |                            4. Sap Xep                                       |\n")
            print("\t\t\t |                            5. Tim Kiem Theo Khoang Gia                      |\n")
            print("\t\t\t |                            6. Thoat                                         |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiQuan.MenuQuanLiQuan()
                    break
                elif chon == 1:
                    QuanLiThucDon.ThucDon()
                elif chon == 2:
                    QuanLiThucDon.MenuThem()
                elif chon == 3:
                    QuanLiThucDon.MenuXoa()
                elif chon == 4:
                    QuanLiThucDon.MenuThuTuSapXep()
                elif chon == 5:
                    QuanLiThucDon.MenuTimKiem()
                elif chon == 6:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def MenuThem():
        chon = None
        while True:
            print("\t\t\t |===================================Them Mon==================================|\n")
            print("\t\t\t |                                 0. Quay Lai                                 |\n")
            print("\t\t\t |                                 1. Thuc An                                  |\n")
            print("\t\t\t |                                 2. Thuc Uong                                |\n")
            print("\t\t\t |                                 3. Thoat                                    |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiThucDon.MenuQuanLiThucDon()
                    break
                elif chon == 1:
                    QuanLiThucDon.ThemThucAn()
                elif chon == 2:
                    QuanLiThucDon.ThemThucUong()
                elif chon == 3:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def MenuXoa():
        chon = None
        while True:
            print("\t\t\t |===================================Xoa Mon===================================|\n")
            print("\t\t\t |                                 0. Quay Lai                                 |\n")
            print("\t\t\t |                                 1. Thuc An                                  |\n")
            print("\t\t\t |                                 2. Thuc Uong                                |\n")
            print("\t\t\t |                                 3. Thoat                                    |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiThucDon.MenuQuanLiThucDon()
                    break
                elif chon == 1:
                    QuanLiThucDon.XoaThucAn()
                elif chon == 2:
                    QuanLiThucDon.XoaThucUong()
                elif chon == 3:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def MenuThuTuSapXep():
        chon = None
        while True:
            print("\t\t\t |===================================Sap Xep===================================|\n")
            print("\t\t\t |                                 0. Quay Lai                                 |\n")
            print("\t\t\t |                                 1. Tang Dan                                 |\n")
            print("\t\t\t |                                 2. Giam Dan                                 |\n")
            print("\t\t\t |                                 3. Thoat                                    |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiThucDon.MenuQuanLiThucDon()
                    break
                elif chon == 1:
                    QuanLiThucDon.MenuSapXep(chon)
                elif chon == 2:
                    QuanLiThucDon.MenuSapXep(chon)
                elif chon == 3:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def MenuSapXep(flag):
        chon = None
        while True:
            if flag == 1:
                print("\t\t\t |===============================Sap Xep Tang Dan==============================|\n")
            elif flag == 2:
                print("\t\t\t |===============================Sap Xep Giam Dan==============================|\n")
            print("\t\t\t |                                 0. Quay Lai                                 |\n")
            print("\t\t\t |                                 1. Thuc Don                                 |\n")
            print("\t\t\t |                                 2. Thuc An                                  |\n")
            print("\t\t\t |                                 3. Thuc Uong                                |\n")
            print("\t\t\t |                                 4. Thoat                                    |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiThucDon.MenuThuTuSapXep()
                    break
                elif chon == 1:
                    lTD = QuanLiThucDon.SapXep(flag, QuanLiThucDon.lThucPham)
                    if flag == 1:
                        print("Danh Sach Mon Tang Dan Theo Gia: ")
                    else:
                        print("Danh Sach Mon Giam Dan Theo Gia: ")
                    QuanLiThucDon.HienThi(lTD)
                elif chon == 2:
                    lTA = QuanLiThucDon.SapXep(flag, QuanLiThucDon.lThucAn)
                    if flag == 1:
                        print("Danh Sach Thuc An Tang Dan Theo Gia: ")
                    else:
                        print("Danh Sach Thuc An Giam Dan Theo Gia: ")
                    QuanLiThucDon.HienThi(lTA)
                elif chon == 3:
                    lTU = QuanLiThucDon.SapXep(flag, QuanLiThucDon.lThucUong)
                    if flag == 1:
                        print("Danh Sach Thuc Uong Tang Dan Theo Gia: ")
                    else:
                        print("Danh Sach Thuc Uong Giam Dan Theo Gia: ")
                    QuanLiThucDon.HienThi(lTU)
                elif chon == 4:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def MenuTimKiem():
        chon = None
        while True:
            print("\t\t\t |===================================Tim Kiem==================================|\n")
            print("\t\t\t |                                 0. Quay Lai                                 |\n")
            print("\t\t\t |                                 1. Thuc Don                                 |\n")
            print("\t\t\t |                                 2. Thuc An                                  |\n")
            print("\t\t\t |                                 3. Thuc Uong                                |\n")
            print("\t\t\t |                                 4. Thoat                                    |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiThucDon.MenuQuanLiThucDon()
                    break
                elif chon == 1:
                    Gia1 = int(input("Gia 1: "))
                    Gia2 = int(input("Gia 2: "))
                    lTD = QuanLiThucDon.TimKiemTheoKhoangGia(Gia1, Gia2, QuanLiThucDon.lThucPham)
                    if lTD:
                        print(f"Danh Sach Mon Gia Tu {Gia1} - {Gia2}: ")
                        QuanLiThucDon.HienThi(lTD)
                    else:
                        print(f"Khong Co Mon Nao Trong Khoang {Gia1} - {Gia2}")
                elif chon == 2:
                    Gia1 = int(input("Gia 1: "))
                    Gia2 = int(input("Gia 2: "))
                    lTA = QuanLiThucDon.TimKiemTheoKhoangGia(Gia1, Gia2, QuanLiThucDon.lThucAn)
                    if lTA:
                        print(f"Danh Sach Thuc An Gia Tu {Gia1} - {Gia2}: ")
                        QuanLiThucDon.HienThi(lTA)
                    else:
                        print(f"Khong Co Thuc An Nao Trong Khoang {Gia1} - {Gia2}")
                elif chon == 3:
                    Gia1 = int(input("Gia 1: "))
                    Gia2 = int(input("Gia 2: "))
                    lTU = QuanLiThucDon.TimKiemTheoKhoangGia(Gia1, Gia2, QuanLiThucDon.lThucUong)
                    if lTU:
                        print(f"Danh Sach Thuc Uong Gia Tu {Gia1} - {Gia2}: ")
                        QuanLiThucDon.HienThi(lTU)
                    else:
                        print(f"Khong Co Thuc Uong Nao Trong Khoang {Gia1} - {Gia2}")
                elif chon == 4:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")