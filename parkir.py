def tarif_parkir(jenis_kendaraan, jam_masuk, jam_keluar):
  difference = jam_keluar - jam_masuk - ((jam_keluar//100 - jam_masuk//100)*40)
  durasi_parkir = (difference // 60) + 1

  if jenis_kendaraan == 1:
    tarif = 3000 + 2000 * (durasi_parkir-1)
  elif jenis_kendaraan == 2:
    tarif = 2000 * durasi_parkir
  return tarif

jumlah_parkir = 30
parkir_occupied = 20
parkir_kosong = jumlah_parkir - parkir_occupied
list_kartu = ["SP01", "SP02", "SP03", "SP04", "SP05"]
print("===================================================================") 
print("                 Selamat datang di Skyland Park!")
print(f"                 Parkiran kosong saat ini: {parkir_kosong}")
print("===================================================================")
print()
if (parkir_kosong == 0):
  print("Mohon maaf, parkiran saat ini sedang penuh.")
  print()
  print("===================================================================")

valid = False
while (not valid and parkir_kosong > 0):
  print("Pilih metode parkir:")
  print("(1) Kartu Apartemen")
  print("(2) Tiket")
  tipe_entrant = int(input())
  print("===================================================================")
  print()

  if (tipe_entrant == 1): # Metode VIP
    nomor_kartu = str(input("Masukkan nomor kartu akses apartemen: "))
    for i in range(len(list_kartu)):
      if list_kartu[i] == nomor_kartu:
        print("Silahkan masuk.")
        print()
        print("===================================================================")
        print()
        print("Terima kasih telah menggunakan jasa parkir apartemen Skyland Park.")
        print()
        print("===================================================================")
        valid = True   
    if valid == False:
      print("Nomor kartu tidak ditemukan!")
      print("===================================================================")
      print()

  if (tipe_entrant == 2): # Metode Non-VIP
    valid = True
    print("Pilih jenis kendaraan:")
    print("(1) Mobil")
    print("(2) Motor")
    jenis_kendaraan = int(input())
    print("===================================================================")
    print()

    jam_masuk = int(input("Masukkan jam masuk parkir (Contoh: 0900, 1730): "))
    print("Silahkan masuk.")
    print()
    print("===================================================================")
    print()

    jam_keluar = int(input("Masukkan jam keluar parkir(Contoh: 0900, 1730): "))
    
    print(f"Silahkan membayar tarif parkir sebesar Rp {tarif_parkir(jenis_kendaraan, jam_masuk, jam_keluar)}")
    print()
    print("===================================================================")
    print()
    print("Terima kasih telah menggunakan jasa parkir apartemen Skyland Park.")
    print()
    print("===================================================================")