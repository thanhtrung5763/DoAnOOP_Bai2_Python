from quanliquan import QuanLiQuan
class QuanLiBoPhan:
    lBoPhan = []

    @staticmethod
    def HienThi():
        print("\t\t\t ----------------DANH SACH BO PHAN----------------")
        print("\t\t\t Ma Bo Phan                          | Ten Bo Phan")
        print("\t\t\t -------------------------------------------------")
        for bp in QuanLiBoPhan.lBoPhan:
            bp.HienThi()
    
    @staticmethod
    def MenuQuanLiBoPhan():
        chon = None
        while True:
            print("\t\t\t |===============================Quan Li Bo Phan===============================|\n")
            print("\t\t\t |                            0. Quay Lai                                      |\n")
            print("\t\t\t |                            1. Danh Sach Bo Phan                             |\n")
            print("\t\t\t |                            2. Thoat                                         |\n")
            print("\t\t\t |===================================CHOOSE====================================|\n")
            try:
                chon = int(input("Ban Chon: "))
            except ValueError:
                print("Vui Long Nhap Chu So")
            else:
                if chon == 0:
                    QuanLiQuan.MenuQuanLiQuan()
                    break
                elif chon == 1:
                    QuanLiBoPhan.HienThi()
                elif chon == 2:
                    exit(0)
                else:
                    print("Vui Long Nhap Lai")
                
        