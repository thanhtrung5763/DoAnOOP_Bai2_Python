from datetime import datetime
from quanlibophan import QuanLiBoPhan
from bophan import BoPhan
from quanlinhanvien import QuanLiNhanVien

class NhanVien:
    ID = 0

    def __init__(self, HoTen=None, GioiTinh=None, QueQuan=None, NgayVaoLam='01/01/0001', NgaySinh='01/01/0001', TenBoPhan=None):
        NhanVien.ID += 1
        self.MaNV = str(NhanVien.ID)
        self.HoTen = HoTen
        self.GioiTinh = GioiTinh
        self.QueQuan = QueQuan
        self.NgaySinh = datetime.strptime(NgaySinh, '%d/%m/%Y')
        self.NgayVaoLam = datetime.strptime(NgayVaoLam, '%d/%m/%Y')
        for bp in QuanLiBoPhan.lBoPhan:
            if bp.TenBP == TenBoPhan:
                self.ViTri = bp
                break
        QuanLiNhanVien.lNhanVien.append(self)

    def TaoNhanVien(self):
        self.MaNV = str(NhanVien.ID)
        self.HoTen = input("Nhap Ho Ten Nhan Vien: ")
        self.GioiTinh = input("Nhap Gioi Tinh: ")
        self.QueQuan = input("Nhap Que Quan: ")
        self.NgayVaoLam = datetime.strptime(input("Nhap Ngay Vao Lam: "), '%d/%m/%Y')
        self.NgaySinh = datetime.strptime(input("Nhap Ngay Sinh: "), '%d/%m/%Y')
        TenBoPhan = input("Nhap Bo Phan Lam Viec: ")
        bp = next((x for x in QuanLiBoPhan.lBoPhan if x.TenBP == TenBoPhan), None)
        if bp != None:
            self.ViTri = bp
            
    def HienThi(self):
        print(f"\t\t\t {self.MaNV:<12} | {self.HoTen:<20} | {self.GioiTinh:<9} | {self.QueQuan:<12} | {self.NgaySinh.strftime('%d/%m/%Y'):<13} | {self.NgayVaoLam.strftime('%d/%m/%Y'):<16} | {self.ViTri.TenBP:<7}")
    
    

