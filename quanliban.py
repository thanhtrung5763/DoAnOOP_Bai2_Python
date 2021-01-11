from quanliquan import QuanLiQuan
class QuanLiBan:
    lBan = []

    @staticmethod
    def HienThi():
        print("\t\t\t Ma Ban                          | Tinh Trang                         | Suc Chua")
        print("\t\t\t -------------------------------------------------------------------------------")
    
    @staticmethod
    def ThemBan():
        from ban import Ban
        b = Ban()
        b.TaoThemBan()
    @staticmethod
    def XoaBan():
        from ban import Ban
        MaBan = input("Nhap Ma Ban Muon Xoa: ")
        b = next((x for x in QuanLiBan.lBan if x.MaBan == MaBan), None)
        if b != None:
            QuanLiBan.lBan.remove(b)
        else:
            print("Khong Tim Thay")
    
    @staticmethod
    def MenuCapNhat():
        from capnhat import CapNhat
        chon = None
        while True:
            print("\t\t\t |=============================Cap Nhat Thong Tin Ban=============================|\n")
            print("\t\t\t |                            0. Quay Lai                                         |\n")
            print("\t\t\t |                            1. Tinh Trang                                       |\n")
            print("\t\t\t |                            2. Suc Chua                                         |\n")
            print("\t\t\t |                            3. Thoat                                            |\n")
            print("\t\t\t |====================================CHOOSE======================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiBan.MenuQuanLiBan()
                    break
                if chon == 3:
                    exit(0)
                elif chon > 0 and chon < 3:
                    MaBan = input("Ma Ban Can Cap Nhat: ")
                    b = next((x for x in QuanLiBan.lBan if x.MaBan == MaBan), None)
                    if b == None:
                        print("Ban Khong Co Trong He Thong")
                    else:
                        print("Thong Tin Ban Can Cap Nhat: ")
                        QuanLiBan.HienThi()
                        b.HienThi()
                        if chon == 1:
                            tt = input("Tinh Trang Moi(Trong/Day): ")
                            if tt == "Day" and b.TinhTrang == "Trong":
                                QuanLiBan.DatBan(b)
                            CapNhat.TinhTrang(b, tt)
                        elif chon == 2:
                            sc = input("Suc Chua Moi: ")
                            CapNhat.SucChua(b, sc)
                        print("Thong Tin Ban Sau Cap Nhat: ")
                        QuanLiBan.HienThi()
                        b.HienThi()
                else:
                    print("Vui Long Nhap Lai")

    @staticmethod
    def DatBan(b):
        from hoadon import HoaDon
        hd = HoaDon()
        hd.TaoHoaDon(b)
    
    @staticmethod
    def MenuQuanLiBan():
        from capnhat import CapNhat   
        chon = None
        while True:
            print("\t\t\t |=================================Quan Li Ban=================================|\n")
            print("\t\t\t |                            0. Quay Lai                                      |\n")
            print("\t\t\t |                            1. Danh Sach Ban                                 |\n")
            print("\t\t\t |                            2. Dat Ban                                       |\n")
            print("\t\t\t |                            3. Them Ban                                      |\n")
            print("\t\t\t |                            4. Xoa Ban                                       |\n")
            print("\t\t\t |                            5. Cap Nhat Thong Tin Ban                        |\n")
            print("\t\t\t |                            6. Xem Hoa Hon                                   |\n")
            print("\t\t\t |                            7. Thoat                                         |\n")
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
                    print("\t\t\t ---------------------------------Danh Sach Ban---------------------------------\n")
                    QuanLiBan.HienThi()
                    for b in QuanLiBan.lBan:
                        b.HienThi()
                elif chon == 2:
                    MaBan = input("Ma Ban Muon Dat: ")
                    b = next((x for x in QuanLiBan.lBan if x.MaBan == MaBan), None)
                    if b == None:
                        print("Ban Khong Co Trong He Thong")
                    else:
                        if b.TinhTrang == "Day":
                            print("Ban Da Day. Vui Long Chon Ban Khac")
                        else:
                            CapNhat.TinhTrang(b, "Day")
                            QuanLiBan.DatBan(b)
                elif chon == 3:
                    QuanLiBan.ThemBan()
                elif chon == 4:
                    QuanLiBan.XoaBan()
                elif chon == 5:
                    QuanLiBan.MenuCapNhat()
                elif chon == 6:
                    from quanlihoadon import QuanLiHoaDon
                    mb = input("Ma Ban: ")
                    hd = next((x for x in QuanLiHoaDon.lHoaDon if x.bBan.MaBan == mb and x.bBan.TinhTrang == "Day"), None)
                    if hd != None:
                        print(f"\t\t\t ----------------------------------Hoa Don Ban {mb}---------------------------------\n")
                        hd.HoaDonChoKhach()
                    else:
                        print("Ban Trong Hoac Khong Tim Thay")
                elif chon == 7:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")