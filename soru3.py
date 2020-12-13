
metin = input('Arama yapılacak metni giriniz: ')
bul = input('Bulunacak ifadeyi yazın: ')

uzunluk = len(bul)
baslaIndex = metin.find(bul)
bitirIndex = baslaIndex + uzunluk
bitirIndex += 1
baslaIndex -= 1

print('Bulunan ifade ve önceki-sonraki harfler: ' + metin[baslaIndex:bitirIndex])