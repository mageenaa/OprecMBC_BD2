totalbelanja = int(input("Masukan total belanja: "))
member = int(input("Apakah anda mempunyai member?\nketik 1 jika anda mempunyai member\nketik 0 jika tidak mempunyai member\n"))

diskon1 = int(totalbelanja-(totalbelanja*(5/100)))
diskon2 = int(totalbelanja-(totalbelanja*(2/100)))
diskon3 = int(totalbelanja-(totalbelanja*(3/100)))
diskon4 = int(totalbelanja-(totalbelanja*(7/100)))
diskon5 = int(totalbelanja-(totalbelanja*(8/100)))
if member == 1:
    if totalbelanja >= 500000 and totalbelanja <= 1000000:
        print("Anda mendapat diskon sebesar 7% sehingga total belanjaan anda menjadi: Rp.",diskon4)
    elif totalbelanja > 1000000:
        print("Anda mendapat diskon sebesar 8% sehingga total belanjaan anda menjadi: Rp.",diskon5)
    else:
        print("Anda mendapat diskon sebesar 5% sehingga total belanjaan anda menjadi: Rp.",diskon1)
elif member == 0:
    if totalbelanja >= 500000 and totalbelanja <= 1000000:
        print("Anda mendapat diskon sebesar 2% sehingga total belanjaan anda menjadi: Rp.",diskon2)
    elif totalbelanja > 1000000:
        print("Anda mendapat diskon sebesar 3% sehingga total belanjaan anda menjadi: Rp.",diskon3)
    else:
        print("Anda tidak mendapat diskon apapun")
else:
    print("\nError")