sayac= 0

for i in range(100, 1000):
    a = int(i / 100)
    b = int((i % 100) / 10)
    c = int(i % 10)
    if (a != b) and (a != c) and (b != c):
        print(i)
        sayac += 1

print("Rakamları farklı 3 basamaklı toplam sayı:", sayac)