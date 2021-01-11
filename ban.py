from quanliban import QuanLiBan
class Ban:
    ID = 0
    def __init__(self, TinhTrang=None, SucChua=None):
        Ban.ID += 1
        self.MaBan = 'B' + str(Ban.ID)
        self.TinhTrang = TinhTrang
        self.SucChua = SucChua
        QuanLiBan.lBan.append(self)
    def TaoThemBan(self):
        self.MaBan = 'B' + str(Ban.ID)
        self.TinhTrang = 'Trong'
        self.SucChua = input("Nhap Suc Chua: ")
    
    def HienThi(self):
        print(f"\t\t\t {self.MaBan:<31} | {self.TinhTrang:<34} | {self.SucChua:<8}")
    