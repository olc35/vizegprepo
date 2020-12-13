
url = []
yasak = ["/", "*", "-", "+", ",", "?", "\\", "}", "{", "=", "]", "[", "(", ")", "&", "%", "$", "#", "£", "!", "\"", ":",
         ";", "<", ">", "|", "'", "^"]
a = False
gir = input('Doğruluğunu kontrol etmek istediğiniz web adresini yazın: ')

url += gir

for i in url:
    if i in yasak:
        a = False
        break
    else:
        for n in url:
            if 'www' and "." in url:
                a = True
                break

if a == True:
    print('URL adresi geçerli')
if a == False:
    print('Geçersiz URL')