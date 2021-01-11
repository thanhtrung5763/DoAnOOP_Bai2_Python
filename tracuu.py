class TraCuu:
    @staticmethod
    def TheoMaNV(MaNV):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.MaNV == MaNV]
        return lNhanVien
    @staticmethod
    def TheoTen(Ten):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.HoTen == Ten]
        return lNhanVien
    @staticmethod
    def TheoGioiTinh(gt):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.GioiTinh == gt]
        return lNhanVien
    @staticmethod
    def TheoQueQuan(qq):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.QueQuan == qq]
        return lNhanVien
    @staticmethod
    def TheoNamVaoLam(nvl):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.NgayVaoLam.strftime('%Y') == nvl]
        return lNhanVien
    @staticmethod
    def TheoNamSinh(ns):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.NgaySinh.strftime('%Y') == ns]
        return lNhanVien
    @staticmethod
    def TheoBoPhan(bp):
        from quanlinhanvien import QuanLiNhanVien
        lNhanVien = [x for x in QuanLiNhanVien.lNhanVien if x.ViTri.TenBP == bp]
        return lNhanVien
    