class QuanLiQuan:

    @staticmethod
    def MenuQuanLiQuan():
        chon = None
        while True:
            print("\t\t\t |=============================Quan Li Quan Ca Phe=============================|\n")
            print("\t\t\t |                            0. Quan Li Nhan Vien                             |\n")
            print("\t\t\t |                            1. Quan Li Ban                                   |\n")
            print("\t\t\t |                            2. Quan Li Bo Phan                               |\n")
            print("\t\t\t |                            3. Quan Li Thuc Don                              |\n")
            print("\t\t\t |                            4. Quan Li Hoa Don                               |\n")
            print("\t\t\t |                            5. Thoat                                         |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    from quanlinhanvien import QuanLiNhanVien
                    QuanLiNhanVien.MenuQuanLiNhanVien()
                elif chon == 1:
                    from quanliban import QuanLiBan
                    QuanLiBan.MenuQuanLiBan()
                elif chon == 2:
                    from quanlibophan import QuanLiBoPhan
                    QuanLiBoPhan.MenuQuanLiBoPhan()
                    pass
                elif chon == 3:
                    from quanlithucdon import QuanLiThucDon
                    QuanLiThucDon.MenuQuanLiThucDon()
                elif chon == 4:
                    from quanlihoadon import QuanLiHoaDon
                    QuanLiHoaDon.MenuQuanLiHoaDon()
                elif chon == 5:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")