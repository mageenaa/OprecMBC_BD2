n = int(input("Masukkan nilai n : "))
def pola(n, m):
     
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i == 1 or i == n or j == 1 or j == m):
                print("* ", end=" ")
            else:
                print("# ", end=" ")
        print("\n")

baris = n
kolom = n
pola(baris, kolom)