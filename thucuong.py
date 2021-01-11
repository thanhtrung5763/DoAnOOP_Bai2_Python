from thucpham import ThucPham
from quanlithucdon import QuanLiThucDon
class ThucUong(ThucPham):

    def __init__(self, Ten=None, Gia=0, TinhTrang=None, ThoiDiemBan=None, Da=None):
        super().__init__(Ten, Gia, TinhTrang, ThoiDiemBan)
        self.Da = Da
        QuanLiThucDon.lThucPham.append(self)
        QuanLiThucDon.lThucUong.append(self)

    def TaoThucUong(self):
        super().TaoMonAn()
        self.Da = input("Da Hay Khong Da: ")
    
    def HienThi(self):
        super().HienThi()
        print(f"{self.Da:<10}")