#Elvyona Pesulima(202352061)
#Sitti R. Alfakhirah Peluw(202351001)
#sarita Rumasukun(202351081)
#Glafia Latekay

def hitung_harga_boneka(jumlah_boneka):
  if jumlah_boneka <= 12:
    harga_per_boneka = 20000
  elif jumlah_boneka <= 24:
    harga_per_boneka = 19500
  elif jumlah_boneka <= 50:
    harga_per_boneka = 18000
  else:
    harga_per_boneka = 17000

  total_harga = jumlah_boneka * harga_per_boneka
  return total_harga

#Meminta input dari pengguna
jumlah_boneka = int(input("Masukkan jumlah boneka yang ingin dibeli: "))

#Memanggil fungsi untuk menghitung harga
total_harga = hitung_harga_boneka(jumlah_boneka)

#Menampilkan hasil
print("Total harga yang harus dibayar adalah Rp.", total_harga)


