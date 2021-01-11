class ThucPham:
    
    def __init__(self, Ten, Gia, TinhTrang, ThoiDiemBan):
        self.Ten = Ten
        self.Gia = Gia
        self.TinhTrang = TinhTrang
        self.ThoiDiemBan = ThoiDiemBan

    def TaoMonAn(self):
        self.Ten = input("Nhap Ten Thuc Pham: ")
        self.Gia = int(input("Nhap Gia: "))
        self.TinhTrang = input("Nhap Tinh Trang(Con/Het): ")
        self.ThoiDiemBan = input("Nhap Thoi Diem Ban(Sang/Trua/Chieu/Toi): ")
    
    def HienThi(self):
        print(f"\t\t\t {self.Ten:<19} | {self.Gia:<8} | {self.TinhTrang:<10} | {self.ThoiDiemBan:<24} | ", end='')
    