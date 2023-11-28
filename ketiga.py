print("---Algorithm Calculator---")
inputUser1 = input("Masukkan logika pertama (true/false) : ").lower()
inputUser2 = input("Masukkan logika kedua (true/false) : ").lower()

# Menggunakan lower() untuk mengonversi input menjadi huruf kecil
inputUser1 = inputUser1 == 'true'
inputUser2 = inputUser2 == 'true'

# Melakukan operasi OR pada nilai boolean
print("hasil OR : ", inputUser1 or inputUser2)
# Melakukan operasi AND pada nilai boolean
print("hasil AND : ", inputUser1 and inputUser2)
