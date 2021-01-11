from quanlibophan import QuanLiBoPhan

class BoPhan:
    ID = 0
    
    def __init__(self, TenBoPhan=None):
        BoPhan.ID += 1
        self.MaBP = str(BoPhan.ID)
        self.TenBP = TenBoPhan
        QuanLiBoPhan.lBoPhan.append(self)

    def HienThi(self):
        print(f"\t\t\t {self.MaBP:<35} | {self.TenBP:<10}")