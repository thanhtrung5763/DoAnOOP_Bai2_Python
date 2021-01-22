from tracuu import TraCuu
from capnhat import CapNhat
from quanliquan import QuanLiQuan
class QuanLiNhanVien:
    lNhanVien = []

    @staticmethod
    def ThemNhanVien():
        from nhanvien import NhanVien
        nv = NhanVien()
        nv.TaoNhanVien()

    @staticmethod
    def XoaNhanVien():
        MaNV = input("Nhap Ma Nhan Vien: ")
        for nv in QuanLiNhanVien.lNhanVien:
            if nv.MaNV == MaNV:
                QuanLiNhanVien.lNhanVien.remove(nv)
    

    @staticmethod
    def MenuQuanLiNhanVien():
        chon = None
        while True:
            print("\t\t\t |==============================Quan Li Nhan Vien==============================|\n")
            print("\t\t\t |                            0. Quay Lai                                      |\n")
            print("\t\t\t |                            1. Danh Sach Nhan Vien                           |\n")
            print("\t\t\t |                            2. Them Nhan Vien                                |\n")
            print("\t\t\t |                            3. Xoa Nhan Vien                                 |\n")
            print("\t\t\t |                            4. Cap Nhat Thong Tin Nhan Vien                  |\n")
            print("\t\t\t |                            5. Tra Cuu Thong Tin Nhan Vien                   |\n")
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
                    print("\t\t\t --------------------------------------------DANH SACH NHAN VIEN--------------------------------------------")
                    print("\t\t\t Ma Nhan Vien | Ho Ten               | Gioi Tinh | Que Quan     | Ngay Sinh     | Ngay Vao Lam     | Bo Phan")
                    print("\t\t\t -----------------------------------------------------------------------------------------------------------")
                    for nv in QuanLiNhanVien.lNhanVien:
                        nv.HienThi()
                elif chon == 2:
                    QuanLiNhanVien.ThemNhanVien()
                elif chon == 3:
                    QuanLiNhanVien.XoaNhanVien()
                elif chon == 4:
                    QuanLiNhanVien.MenuCapNhat()
                elif chon == 5:
                    QuanLiNhanVien.MenuTraCuu()
                elif chon == 6:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")

    @staticmethod
    def MenuCapNhat():
        chon = None
        while True:
            print("\t\t\t |=============================Cap Nhat Thong Tin Nhan Vien=============================|\n")
            print("\t\t\t |                            0. Quay Lai                                               |\n")
            print("\t\t\t |                            1. Cap Nhat Ho Ten                                        |\n")
            print("\t\t\t |                            2. Cap Nhat Gioi Tinh                                     |\n")
            print("\t\t\t |                            3. Cap Nhat Que Quan                                      |\n")
            print("\t\t\t |                            4. Cap Nhat Ngay Vao Lam                                  |\n")
            print("\t\t\t |                            5. Cap Nhat Ngay Sinh                                     |\n")
            print("\t\t\t |                            6. Cap Nhat Ngay Vi Tri                                   |\n")
            print("\t\t\t |                            7. Thoat                                                  |\n")
            print("\t\t\t |========================================CHOOSE========================================|\n")
            
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiNhanVien.MenuQuanLiNhanVien()
                    break
                if chon == 7:
                    exit(0)
                elif chon > 0 and chon < 7:
                    MaNV = input("Ma Nhan Vien Can Cap Nhat: ")
                    nv = next((x for x in QuanLiNhanVien.lNhanVien if x.MaNV == MaNV), None)
                    if nv == None:
                        print("Nhan Vien Khong Co Trong He Thong")
                        QuanLiNhanVien.MenuQuanLiNhanVien()
                    else:
                        print("Thong Tin Nhan Vien Can Cap Nhat: ")
                        print("\t\t\t Ma Nhan Vien | Ho Ten               | Gioi Tinh | Que Quan     | Ngay Sinh     | Ngay Vao Lam     | Bo Phan")
                        nv.HienThi()
                        if chon == 1:
                            HoTen = input("Ho Ten Moi: ")
                            CapNhat.HoTen(nv, HoTen)
                        elif chon == 2:
                            GioiTinh = input("Gioi Tinh Moi: ")
                            CapNhat.GioiTinh(nv, GioiTinh)
                        elif chon == 3:
                            QueQuan = input("Que Quan Moi: ")
                            CapNhat.QueQuan(nv, QueQuan)
                        elif chon == 4:
                            NgayVaoLam = input("Ngay Vao Lam Moi: ")
                            CapNhat.NgayVaoLam(nv, NgayVaoLam)
                        elif chon == 5:
                            NgaySinh = input("Ngay Sinh Moi: ")
                            CapNhat.NgaySinh(nv, NgaySinh)
                        elif chon == 6:
                            TenBP = input("Ten Vi Tri Moi: ")
                            CapNhat.ViTri(nv, TenBP)
                        print("Thong Tin Nhan Vien Can Cap Nhat: ")
                        print("\t\t\t Ma Nhan Vien | Ho Ten               | Gioi Tinh | Que Quan     | Ngay Sinh     | Ngay Vao Lam     | Bo Phan")
                        nv.HienThi()
                else:
                    print("Vui Long Nhap Lai")
                    

    @staticmethod
    def MenuTraCuu():
        chon = None
        while True:
            print("\t\t\t |=============================Tra Cuu Thong Tin Nhan Vien=============================|\n")
            print("\t\t\t |                            0. Quay Lai                                              |\n")
            print("\t\t\t |                            1. Theo Ma Nhan Vien                                     |\n")
            print("\t\t\t |                            2. Theo Ten                                              |\n")
            print("\t\t\t |                            3. Theo Gioi Tinh                                        |\n")
            print("\t\t\t |                            4. Theo Que Quan                                         |\n")
            print("\t\t\t |                            5. Theo Nam Vao Lam                                      |\n")
            print("\t\t\t |                            6. Theo Nam Sinh                                         |\n")
            print("\t\t\t |                            7. Theo Vi Tri                                           |\n")
            print("\t\t\t |                            8. Thoat                                                 |\n")
            print("\t\t\t |=======================================CHOOSE========================================|\n")
            
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                lNhanVien = []
                if chon == 0:
                    QuanLiNhanVien.MenuQuanLiNhanVien()
                    break
                if chon == 1:
                    MaNV = input("Ma Nhan Vien Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoMaNV(MaNV)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 2:
                    Ten = input("Ten Nhan Vien Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoTen(Ten)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 3:
                    GioiTinh = input("Gioi Tinh Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoGioiTinh(GioiTinh)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 4:
                    QueQuan = input("Que Quan Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoQueQuan(QueQuan)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 5:
                    NamVaoLam = input("Nam Vao Lam Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoNamVaoLam(NamVaoLam)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 6:
                    NamSinh = input("Nam Sinh Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoNamSinh(NamSinh)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 7:
                    TenBP = input("Ten Bo Phan Muon Tra Cuu: ")
                    lNhanVien = TraCuu.TheoBoPhan(TenBP)
                    if lNhanVien:
                        QuanLiNhanVien.HienThi(lNhanVien)
                    else:
                        print("Khong Tim Thay")
                elif chon == 8:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
    
    @staticmethod
    def HienThi(lNhanVien):
        print("\t\t\t Ma Nhan Vien | Ho Ten               | Gioi Tinh | Que Quan     | Ngay Sinh     | Ngay Vao Lam     | Bo Phan")
        for nv in lNhanVien:
            nv.HienThi()


                