from nhanvien import NhanVien
from bophan import BoPhan
from quanliquan import QuanLiQuan
from quanlinhanvien import QuanLiNhanVien
from quanlihoadon import QuanLiHoaDon
from quanlibophan import QuanLiBoPhan
from quanlithucdon import QuanLiThucDon
from quanliban import QuanLiBan
from hoadon import HoaDon
from thucan import ThucAn
from thucuong import ThucUong
from ban import Ban

bp1 = BoPhan("Quan Li")
bp2 = BoPhan("Phuc Vu")
bp3 = BoPhan("Pha Che")
bp4 = BoPhan("Thu Ngan")

nv1 = NhanVien("Pham Trung Thanh", "Nam", "Dong Nai", "20/09/2020", "12/03/2001", "Phuc Vu")
nv2 = NhanVien("Pham Van A", "Nam", "HCM", "21/10/2020", "14/02/2001", "Thu Ngan")
nv3 = NhanVien("Dao Bich Tram", "Nu", "Ha Noi", "02/03/2020", "17/09/1999", "Thu Ngan")
nv4 = NhanVien("Le Trung Hieu", "Nam", "Nghe An", "14/07/2020", "19/11/1990", "Quan Li")
nv5 = NhanVien("Phan Yen Nhi", "Nu", "Ha Noi", "09/01/2020", "21/07/2001", "Pha Che")

f1 = ThucAn("Egg Tart", 30000, "Con", "Sang, Trua, Chieu", "Chay")
f2 = ThucAn("Bap Xao", 15000, "Het", "Sang, Trua", "Chay")
f3 = ThucAn("Com Tam", 20000, "Con", "Sang, Trua, Chieu", "Khong Chay")
f4 = ThucAn("Com Chay", 15000, "Con", "Trua, Chieu", "Chay")
f5 = ThucAn("Goi Bo", 20000, "Con", "Chieu, Toi", "Khong Chay")
d1 = ThucUong("Tra Sua Tran Chau", 30000, "Con", "Sang, Trua, Chieu, Toi", "Da")
d2 = ThucUong("Sua Nong", 20000, "Con", "Trua, Toi", "Khong Da")
d3 = ThucUong("Coffee Da", 15000, "Con", "Sang, Toi", "Da")
d4 = ThucUong("Coffee", 15000, "Con", "Sang, Toi", "Khong Da")
d5 = ThucUong("Nuoc Cam", 30000, "Con", "Sang, Trua, Chieu", "Da")
# nv1.HienThi()
# nv2.HienThi()
# nv6 = NhanVien()
# nv6.TaoNhanVien()
# nv6.HienThi()
# nv1.CapNhatViTri("Quan Li")
# nv1.HienThi()
b1 = Ban("Trong", 4)
b2 = Ban("Trong", 2)
b3 = Ban("Trong", 2)
b4 = Ban("Day", 4)
b5 = Ban("Day", 6)

sl1 = [1, 2, 3]
sl2 = [2, 1, 3]
sl3 = [1, 4]
sl4 = [1, 3, 2, 4]
sl5 = [2, 1, 3, 2]
tp1 = [f1, f4, d5]
tp2 = [f2, f1, d5]
tp3 = [d5, f3]
tp4 = [d4, f1, d3, f5]
tp5 = [d1, d2, f4, f2]
hd3 = HoaDon("2", tp3, sl3, b3, "05/09/2020", "Sang", 200000)
hd1 = HoaDon("2", tp1, sl1, b2, "05/01/2021", "Trua", 100000)
hd2 = HoaDon("3", tp2, sl2, b1, "07/12/2020", "Sang", 500000)

hd4 = HoaDon("2", tp4, sl4, b4, "27/01/2021", "Trua", 300000)
hd5 = HoaDon("3", tp5, sl5, b5, "27/01/2021", "Toi", 200000)
QuanLiQuan.MenuQuanLiQuan()

