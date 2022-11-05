total = int(input("Masukkan Total Belanja : "))
member = input("Apakah anda member? (y/t)")

if member==("y"):
    if(total>=500000 and total<=1000000):
        print("\nSelamat anda mendapatkan diskon 7%")
        new_total = total * (0.07)
        diskon1 = total-new_total
        print("\nTotal belanja anda adalah : ",diskon1)
    elif(total>1000000):
        print("\nSelamat anda mendapatkan diskon 8%")
        new_total = total * (0.08)
        diskon2 = total-new_total
        print("\nTotal belanja anda adalah : ",diskon2)
    else:
        print("\nSelamat anda mendapatkan diskon 5%")
        new_total = total*(0.05)
        diskon3 = total-new_total
        print("\nTotal belanja anda adalah : ",diskon3)

elif member==("t"):
    if(total>=500000 and total<=1000000):
        print("\nSelamat anda mendapatkan diskon 2%")
        new_total = total * (0.02)
        diskon4 = total-new_total
        print("\nTotal belanja anda adalah : ",diskon4)
    elif(total>1000000):
        print("\nSelamat anda mendapatkan diskon 3%")
        new_total = total * (0.03)
        diskon5 = total-new_total
        print("\nTotal belanja anda adalah : ",diskon5)
else:
    print("Data tidak ditemukan")