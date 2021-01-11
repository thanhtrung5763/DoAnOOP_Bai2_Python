from datetime import datetime
from quanlibophan import QuanLiBoPhan
from ban import Ban
class CapNhat:
    
    @staticmethod
    def HoTen(nv, ht):
        nv.HoTen = ht
    @staticmethod
    def GioiTinh(nv, gt):
        nv.GioiTinh = gt
    @staticmethod
    def QueQuan(nv, qq):
        nv.QueQuan = qq
    @staticmethod
    def NgayVaoLam(nv, nvl):
        nv.NgayVaoLam = datetime.strptime(nvl, '%d/%m/%Y')
    @staticmethod
    def NgaySinh(nv, ns):
        nv.NgaySinh = datetime.strptime(ns, '%d/%m/%Y')
    @staticmethod
    def ViTri(nv, vt):
        ViTriMoi = next((x for x in QuanLiBoPhan.lBoPhan if x.TenBP == vt), None)
        if ViTriMoi != None:
            nv.ViTri = ViTriMoi
    @staticmethod
    def TinhTrang(b, tt):
        b.TinhTrang = tt
    @staticmethod
    def SucChua(b, sc):
        b.SucChua = sc