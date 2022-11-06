def telkom (seragam):
    match seragam:
        case ("Senin"):
            print("Seragam anda hari ini merah")
        case ("Selasa"):
            print("Seragam anda hari ini putih")
        case ("Rabu"):
            print("Seragam anda hari ini putih")
        case ("Kamis"):
            print("Seragam anda hari ini bebas")
        case ("Jumat"):
            print("Seragam anda hari ini batik")
        case ("Sabtu"):
            print("Seragam anda hari ini bebas")
        case default:
            print("Data tidak ditemukan")
print(telkom(input("Masukkan hari : ")))