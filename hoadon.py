from datetime import datetime
from quanliban import QuanLiBan
from quanlinhanvien import QuanLiNhanVien
from quanlithucdon import QuanLiThucDon
from quanlihoadon import QuanLiHoaDon
class HoaDon:
    ID = 0
    def __init__(self, nv=None, lMon=None, sl=None, b=None, tg='01/01/0001', td=None, tkd=0):
        HoaDon.ID += 1
        self.MaHoaDon = str(HoaDon.ID)
        self.NVThuNgan = next((x for x in QuanLiNhanVien.lNhanVien if x.MaNV == nv), None)
        self.bBan = b
        if lMon == None:
            self.lMon = []
        else:
            self.lMon = lMon
        if b == None:
            self.lSoLuong = []
        else:
            self.lSoLuong = sl
        self.ThoiGian = datetime.strptime(tg, '%d/%m/%Y')
        self.ThoiDiem = td
        self.TienKhachDua = tkd
        QuanLiHoaDon.lHoaDon.insert(0, self)
    def TaoHoaDon(self, b):
        self.MaHoaDon = HoaDon.ID
        self.bBan = b
        mnv = input("Ma Nhan Vien Thu Ngan: ")
        self.NVThuNgan = next((x for x in QuanLiNhanVien.lNhanVien if x.MaNV == mnv), None)
        self.ThoiDiem = input("Thoi Diem(Sang/Trua/Chieu/Toi): ")
        self.ThoiGian = datetime.now()

        slm = int(input("So Luong Mon: "))
        for _ in range(slm):
            tm = input("Ten Mon: ")
            tp = next((x for x in QuanLiThucDon.lThucPham if x.Ten == tm), None)
            sl = int(input("So Luong: "))
            self.lSoLuong.append(sl)
            self.lMon.append(tp)
        print(f"Tong Tien: {self.TinhTien()}")
        tkd = int(input("Tien Khach Dua: "))
        self.TienKhachDua = tkd
    
    def TinhTien(self):
        s = 0
        for i in range(len(self.lSoLuong)):
            s += self.lSoLuong[i] * self.lMon[i].Gia
        return s
    def HoaDonChoKhach(self):
        print("\t\t\t --------------------------------------***--------------------------------------")
        print(f"\t\t\t Thu Ngan: {self.NVThuNgan.HoTen}")
        print(f"\t\t\t Thoi Gian: {self.ThoiDiem} {self.ThoiGian.strftime('%d/%m/%Y')}")
        print("\t\t\t --------------------------------------***--------------------------------------")
        print("\t\t\t Ten                                        S/L          Gia              Tong")
        print("\t\t\t --------------------------------------***--------------------------------------")
        for i in range(len(self.lMon)):
            print(f"\t\t\t {self.lMon[i].Ten:<28}               {self.lSoLuong[i]:<10}   {self.lMon[i].Gia:<10}       {self.lSoLuong[i] * self.lMon[i].Gia:<4}")
        print("\t\t\t --------------------------------------***--------------------------------------")
        print(f"\t\t\t Tong So Luong Mon: {len(self.lMon)}")
        print("\t\t\t --------------------------------------***--------------------------------------")
        print(f"\t\t\t Tong Phai Thanh Toan: {self.TinhTien()}")
        print("\t\t\t --------------------------------------***--------------------------------------")
        print(f"\t\t\t Tien Khach Dua: {self.TienKhachDua}")
        print("\t\t\t --------------------------------------***--------------------------------------")
        print(f"\t\t\t Tra Lai: {self.TienKhachDua - self.TinhTien()}")
    def ThongTinHoaDon(self):
        print(f"\t\t\t {self.MaHoaDon:<13} | {self.ThoiDiem:<10} {self.ThoiGian.strftime('%d/%m/%Y'):<10} | {self.TinhTien():<9}")