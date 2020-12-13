email = []
yasak = ["/", "*", "-", "+", ",", "?", "\\", "}", "{", "=", "]", "[", "(", ")", "&", "%", "$", "#", "£", "!", "\"", ":",
         ";", "<", ">", "|"]
a = False
gir = input('Doğruluğunu kontrol etmek istediğiniz mail adresini yazın: ')

email += gir
if len(email) >= 8:
    for i in email:
        if i in yasak:
            a = False
            break
        else:
            for n in email:
                if '@' and '.' in email:
                    a = True
                break

if a == True:
    print('Mail adresi geçerli')
if a == False:
    print('Geçersiz mail adresi')
