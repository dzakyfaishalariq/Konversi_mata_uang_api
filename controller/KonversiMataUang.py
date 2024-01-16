class KonversiMataUang:
    def __init__(self, nilai):
        self.nilai = nilai
        self.mata_uang_konversi_indonesia = [0.000064, 0.00046, 0.000051, 0.0094, 0.000055, 0.000086, 0.000097]
        self.mata_uang_konversi_Dolar_amerika_serikat = [15611, 7.13, 0.79, 146.42, 0.86, 1.35, 1.51]
        self.mata_uang_konversi_yuan_renminbi = [2191.83, 0.14, 0.11, 20.55, 0.12, 0.19, 0.21]
        self.mata_uang_konversi_pound_steling = [19780.42, 1.27, 9.03, 185.26, 1.09, 1.70, 1.92]
        self.mata_uang_konvers_yen_jepang = [106.63, 0.0068, 0.049, 0.0054, 0.0059, 0.0092, 0.010]
        self.mata_uang_konversi_franc_swiss = [18146.86, 1.16, 8.28, 0.92, 170.24, 1.56, 1.76]
        self.mata_uang_konversi_dolar_kanada = [11602.51, 0.74, 5.29, 0.59, 108.80, 0.64, 1.12]
        self.mata_uang_konversi_dolar_australia = [10315.74, 0.66, 4.71, 0.52, 96.76, 0.57, 0.89]
    def Rupiah(self):
        # mengubah nilai rupiah ke dalam mata uang lain
        rupiah = self.nilai
        hasil = [rupiah*mata_uang for mata_uang in self.mata_uang_konversi_indonesia]
        nama_mata_uang = ["Dolar_Amerika_Serikat", "Yuan_Renminbi", "Pound_Sterling", "Yen_Jepang", "Franc_Swiss", "Dolar_Kanada", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
         
    
    def Dolar_Amerika_Serikat(self):
        # mengubah nilai Dolar_Amerika_Serikat ke dalam mata uang lain
        DAS = self.nilai
        hasil = [DAS*mata_uang for mata_uang in self.mata_uang_konversi_Dolar_amerika_serikat]
        nama_mata_uang = ["Rupiah", "Yuan_Renminbi", "Pound_Sterling", "Yen_Jepang", "Franc_Swiss", "Dolar_Kanada", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    def Yuan_Renminbi(self):
         # mengubah nilai Yuan_Renminbi ke dalam mata uang lain
        YR = self.nilai
        hasil = [YR*mata_uang for mata_uang in self.mata_uang_konversi_yuan_renminbi]
        nama_mata_uang = ["Rupiah", "Dolar_Amerika_Serikat", "Pound_Sterling", "Yen_Jepang", "Franc_Swiss", "Dolar_Kanada", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    def Pound_Sterling(self):
        # mengubah nilai Pound_Sterling ke dalam mata uang lain
        PS = self.nilai
        hasil = [PS*mata_uang for mata_uang in self.mata_uang_konversi_pound_steling]
        nama_mata_uang = ["Rupiah", "Dolar_Amerika_Serikat", "Yuan_Renminbi", "Yen_Jepang", "Franc_Swiss", "Dolar_Kanada", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    def Yen_Jepang(self):
        # mengubah nilai Yen_Jepang ke dalam mata uang lain
        YJ = self.nilai
        hasil = [YJ*mata_uang for mata_uang in self.mata_uang_konvers_yen_jepang]
        nama_mata_uang = ["Rupiah", "Dolar_Amerika_Serikat", "Yuan_Renminbi", "Pound_Sterling", "Franc_Swiss", "Dolar_Kanada", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    def Franc_Swiss(self):
        # mengubah nilai Franc_Swiss dalam mata uang lain
        FS = self.nilai
        hasil = [FS*mata_uang for mata_uang in self.mata_uang_konversi_franc_swiss]
        nama_mata_uang = ["Rupiah", "Dolar_Amerika_Serikat", "Yuan_Renminbi", "Pound_Sterling", "Yen_Jepang", "Dolar_Kanada", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    def Dolar_Kanada(self):
        # mengubah nilai Dolar kanada ke dalam mata uang lain
        DK = self.nilai
        hasil = [DK*mata_uang for mata_uang in self.mata_uang_konversi_dolar_kanada]
        nama_mata_uang = ["Rupiah", "Dolar_Amerika_Serikat", "Yuan_Renminbi", "Pound_Sterling", "Yen_Jepang", "Franc_Swiss", "Dolar_Australia"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    def Dolar_Australia(self):
        # mengubah nilai Dolar Australia ke dalam mata uang lain
        DA = self.nilai
        hasil = [DA*mata_uang for mata_uang in self.mata_uang_konversi_dolar_australia]
        nama_mata_uang = ["Rupiah", "Dolar_Amerika_Serikat", "Yuan_Renminbi", "Pound_Sterling", "Yen_Jepang", "Franc_Swiss", "Dolar_Kanada"]
        data = [
            {
                "nama_mata_uang" : nama_mata_uang[i],
                "nilai":hasil[i]
            }
            for i in range(len(hasil))
        ]
        return data
    
    