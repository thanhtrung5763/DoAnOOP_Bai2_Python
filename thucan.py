from thucpham import ThucPham
from quanlithucdon import QuanLiThucDon
class ThucAn(ThucPham):

    def __init__(self, Ten=None, Gia=0, TinhTrang=None, ThoiDiemBan=None, Chay=None):
        super().__init__(Ten, Gia, TinhTrang, ThoiDiemBan)
        self.Chay = Chay
        QuanLiThucDon.lThucPham.append(self)
        QuanLiThucDon.lThucAn.append(self)

    def TaoThucAn(self):
        super().TaoMonAn()
        self.Chay = input("Nhap Loai Mon(Chay/Khong Chay): ")

    def HienThi(self):
        super().HienThi()
        print(f"{self.Chay:<10}")
