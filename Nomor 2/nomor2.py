totalbelanja = int(input("Masukan total belanja: "))
member = int(input("Apakah anda mempunyai member?\nketik 1 jika anda mempunyai member\nketik 0 jika tidak mempunyai member\n"))

diskon1 = int(totalbelanja-(totalbelanja*(5/100)))
diskon2 = int(totalbelanja-(totalbelanja*(2/100)))
diskon3 = int(totalbelanja-(totalbelanja*(3/100)))
if member == 1:
    print("Anda mendapat diskon sebesar 5% sehingga total belanjaan anda menjadi: Rp.",diskon1)
else:
    if totalbelanja >= 500000:
        print("Anda mendapat diskon sebesar 2% sehingga total belanjaan anda menjadi: Rp.",diskon2)
    elif totalbelanja >= 1000000:
        print("Anda mendapat diskon sebesar 3% sehingga total belanjaan anda menjadi: Rp.",diskon3)
    else:
        print("Anda tidak mendapat diskon apapun")