class Magaza:
    # İnitializer metodu oluşturuldu(değişkenler private olarak tanımlanacaktır)
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__toplam_satis_tutari = 0

    #  Değişkenler için accessor/mutator metotları oluşturuldu
    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    # Mağaza sınıfı içinde bu dictionary üzerinde arama yapma ve satış ile ilgili toplam tutarları bulmayı sağlayan metot
    def magaza_satis_tutar(self, satis_dict):
        self.magaza_toplam_satis = 0
        satici_toplam_satis = 0
        for key, value in satis_dict.items():
            magaza, satici_adi, satici_cinsi = key
            tutar = value
            if magaza == self.__magaza_adi:
                self.magaza_toplam_satis += tutar
                magazalar[magaza] = self.magaza_toplam_satis
            if satici_adi == self.__satici_adi and satici_cinsi == self.__satici_cinsi:
                satici_toplam_satis += tutar
                magazalar[magaza] = self.magaza_toplam_satis
        self.__toplam_satis_tutari = satici_toplam_satis
        return self.magaza_toplam_satis, self.__toplam_satis_tutari

    # Mağaza sınıfı içinde hesapladığınız mağazaların ve satıcıların her biri için toplam satış tutarlarını yazdırmak için __str__ metodu
    def __str__(self):
        return f"{self.__magaza_adi} mağazasında {self.__satici_adi} {self.__satici_cinsi} satarak {self.__toplam_satis_tutari} TL satış yaptı."

# Mağaza adı, satıcının bilgileri (satıcı_adi, satıcı_cinsi) ve satış tutarını klavyeden döngüsel olarak sürekli alan bir main metodu
satis_dict = {}
magazalar = {}

while True:
    
    magaza_adi = input("Mağazanın adını giriniz(çıkış için 'q' girin): ")
    if magaza_adi == "q":
        break
    satici_adi = input("Satıcı adı: ")
    satici_cinsi = input("Satıcı cinsi (tv/bilgisayar/beyaz eşya/diğer): ")
    satis_tutari = int(input("Satış tutarı: "))
    key = (magaza_adi, satici_adi, satici_cinsi)
    if key in satis_dict:
        satis_dict[key] += satis_tutari
    else:
        satis_dict[key] = satis_tutari


for key in satis_dict.keys():

    magaza_adi, satici_adi, satici_cinsi = key
    magaza = Magaza(magaza_adi, satici_adi, satici_cinsi)
    magaza_satis = magaza.magaza_satis_tutar(satis_dict)
    print(magaza.__str__())

for key, value in magazalar.items():
    print(f"{key} mağazası toplam {value} TL satış yaptı.")


