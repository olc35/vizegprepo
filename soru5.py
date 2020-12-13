"""
receive-23-1-0\n
send-181-3-0-1\nreceive-170-3-0\n
receive-150-0-1\n0-4-5-6-\n
"""
islemGir = input("\nlutfen Islem Giriniz: ")
islemGir = islemGir.replace("\\", "n")
girilenIslem = islemGir.split("nn")
girilenIslem.pop()
sayac = 0
for i in girilenIslem:
    sayac += 1
    a = i.split("-")
    if a[0] == "send":
        pass
    elif a[0] == "receive":
        pass
    else:
        print("\n******************************************\n")
        print("Error\n")
        print(sayac, ". Bolum Hatalı Send Veya Receive Icermiyor\n")
        break

for i in girilenIslem:
    if "send" in i:
        a = i.split("-")
        if len(a) == 5:
            send: str = "send"
        elif len(a) < 5:
            print("Error : Send İfadesi Parametreleri Eksik Girilmiş")
            break
        elif len(a) > 5:
            print("Error : Send İfadesi Parametreleri Fazla Girilmiş")
            break
        sinyalGucu = int(a[1])
        if sinyalGucu < 255 and sinyalGucu > 0:
            if sinyalGucu >= 0 and sinyalGucu <= 50:
                sinyalCikti = "Cok Zayıf Siyanl"
            elif sinyalGucu >= 51 and sinyalGucu <= 100:
                sinyalCikti = "Zayıf Sinyal"
            elif sinyalGucu >= 101 and sinyalGucu <= 150:
                sinyalCikti = "Orta Sinyal"
            elif sinyalGucu >= 151 and sinyalGucu <= 200:
                sinyalCikti = "Guclu Sinyal"
            elif sinyalGucu >= 201 and sinyalGucu <= 255:
                sinyalCikti = "Cok Guclu Sinyal"
        else:
            print("Error : Sinyal Gücü Değeri Referans Aralığı Disinda")
            break
        cihaz = int(a[2])
        if cihaz >= 1 and cihaz <= 4:
            if cihaz == 1:
                cihazCikti = "Televizyon"
            elif cihaz == 2:
                cihazCikti = "Camasir Makinesi"
            elif cihaz == 3:
                cihazCikti = "Buzdolabi"
            elif cihaz == 4:
                cihazCikti = "Firin"
        else:
            print("Error : Girilen Cihaz Degeri Yanlis")
            break
        cihazDurumu = int(a[3])
        if cihazDurumu >= 0 and cihazDurumu <= 1:
            if cihazDurumu == 0:
                cihazDurumuCikti = "Off"
            elif cihazDurumu == 1:
                cihazDurumuCikti = "on"
        else:
            print("Error : Cihaz Durumu Degeri Yanlis Girilmis")
            break
        cevap = int(a[4])
        if cevap >= 0 and cevap <= 1:
            if cevap == 0:
                cevapCikti = "Cevap İstenmiyor"
            elif cevap == 1:
                cevapCikti = "Cevap İsteniyor"
        else:
            print("Error : Cihaz Durumu Degeri Yanlis Girilmis")
            break
        print("\n******************************************\n")
        print("Kod Tipi     : ", send, "- Giden")
        print("Sinyal Gucu  : ", sinyalGucu, "-", sinyalCikti)
        print("Cihaz        : ", cihaz, "-", cihazCikti)
        print("Cihaz Durumu : ", cihazDurumu, "-", cihazDurumuCikti)
        print("Cevap        : ", cevap, "-", cevapCikti)
        print("\n******************************************")
    elif "receive" in i:
        a = i.split("-")
        if len(a) == 4:
            receive = "Receive"
        elif len(a) < 5:
            print("Error : Receive İfadesi Parametreleri Eksik Girilmiş")
            break
        elif len(a) > 5:
            print("Error : Receive İfadesi Parametreleri Fazla Girilmiş")
            break
        sinyalGucu = int(a[1])
        if sinyalGucu < 255 and sinyalGucu > 0:
            if sinyalGucu >= 0 and sinyalGucu <= 50:
                sinyalCikti = "Cok Zayıf Siyanl"
            elif sinyalGucu >= 51 and sinyalGucu <= 100:
                sinyalCikti = "Zayıf Sinyal"
            elif sinyalGucu >= 101 and sinyalGucu <= 150:
                sinyalCikti = "Orta Sinyal"
            elif sinyalGucu >= 151 and sinyalGucu <= 200:
                sinyalCikti = "Guclu Sinyal"
            elif sinyalGucu >= 201 and sinyalGucu <= 255:
                sinyalCikti = "Cok Guclu Sinyal"
        else:
            sinyalGucu = "Sinyal Gücü Değeri Referans Aralıgı Disinda"
            break
        cihaz = int(a[2])
        if cihaz >= 1 and cihaz <= 4:
            if cihaz == 1:
                cihazCikti = "Televizyon"
            elif cihaz == 2:
                cihazCikti = "Camasir Makinesi"
            elif cihaz == 3:
                cihazCikti = "Buzdolabi"
            elif cihaz == 4:
                cihazCikti = "Firin"
        else:
            cihaz = "Girilen Cihaz Degeri Yanlis"
            break
        cihazDurumu = int(a[3])
        if cihazDurumu >= 0 and cihazDurumu <= 1:
            if cihazDurumu == 0:
                cihazDurumuCikti = "Off"
            elif cihazDurumu == 1:
                cihazDurumuCikti = "on"
        else:
            cihazDurumuCikti = "Cihaz Durumu Degeri Yanlis Girilmis"
        print("\n******************************************\n")
        print("Kod Tipi     : ", receive, "- Gelen")
        print("Sinyal Gucu  : ", sinyalGucu, "-", sinyalCikti)
        print("Cihaz        : ", cihaz, "-", cihazCikti)
        print("Cihaz Durumu : ", cihazDurumu, "-", cihazDurumuCikti)
        print("\n******************************************\n")

