from quanliquan import QuanLiQuan
class QuanLiHoaDon:
    lHoaDon = []

    @staticmethod
    def TinhTien(lhd):
        return sum(x.TinhTien() for x in lhd)
    
    @staticmethod
    def HienThiHoaDon(lhd):
        print("\t\t\t -----------------DANH SACH HOA DON-----------------")
        print("\t\t\t Ma Hoa Don    | Thoi Gian             | Tong Tien")
        print("\t\t\t ---------------------------------------------------")
        for hd in lhd:
            hd.ThongTinHoaDon()
    @staticmethod 
    def HienThiDoanhThu(lhd):
        print("\t\t\t ---------------------------------------------------")
        print(f"\t\t\t Tong:                                 | {QuanLiHoaDon.TinhTien(lhd), -12}")
        print("\t\t\t ---------------------------------------------------")
    @staticmethod
    def DoanhThuThang(t):
        lhd = [x for x in QuanLiHoaDon.lHoaDon if x.ThoiGian.strftime('%m') == t]
        if lhd:
            print(f"\t\t\t Doanh Thu Thang {t}: ")
            QuanLiHoaDon.HienThiHoaDon(lhd)
            QuanLiHoaDon.HienThiDoanhThu(lhd)
        else:
            print(f"Thang {t} Khong Co Doanh Thu")
    @staticmethod
    def TongDoanhThu():
        print("\t\t\t Tong Doanh Thu: ")
        QuanLiHoaDon.HienThiHoaDon(QuanLiHoaDon.lHoaDon)
        QuanLiHoaDon.HienThiDoanhThu(QuanLiHoaDon.lHoaDon)
    @staticmethod
    def MenuDoanhThu():
        chon = None
        while True:
            print("\t\t\t |==============================Quan Li Doanh Thu==============================|\n")
            print("\t\t\t |                            0. Quay Lai                                      |\n")
            print("\t\t\t |                            1. Theo Thang                                    |\n")
            print("\t\t\t |                            2. Tong Doanh Thu                                |\n")
            print("\t\t\t |                            3. Thoat                                         |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiHoaDon.MenuQuanLiHoaDon()
                elif chon == 1:
                    t = input("Thang Muon Tinh Doanh Thu: ")
                    QuanLiHoaDon.DoanhThuThang(t)
                elif chon == 2:
                    QuanLiHoaDon.TongDoanhThu()
                elif chon == 3:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def MenuQuanLiHoaDon():
        chon = None
        while True:
            print("\t\t\t |===============================Quan Li Hoa Don===============================|\n")
            print("\t\t\t |                            0. Quay Lai                                      |\n")
            print("\t\t\t |                            1. Danh Sach Hoa Don                             |\n")
            print("\t\t\t |                            2. Doanh Thu                                     |\n")
            print("\t\t\t |                            3. Thoat                                         |\n")
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
                    QuanLiHoaDon.HienThiHoaDon(QuanLiHoaDon.lHoaDon)
                elif chon == 2:
                    QuanLiHoaDon.MenuDoanhThu()
                elif chon == 3:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")