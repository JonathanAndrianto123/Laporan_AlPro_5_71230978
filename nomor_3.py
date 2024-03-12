def mata_kuliah(jumlah) :
    nilai_ = 0
    total = 0
    for i in range(1, jumlah + 1) :
        nilai = input(f"Nilai MK {i} = ")
        if nilai == "A" :
            nilai_ += 4
        elif nilai == "B" :
            nilai_ += 3
        elif nilai == "C" :
            nilai_ += 2
        elif nilai == "D" :
            nilai_ += 1
        else :
            print("Nilai invalid")
    total = nilai_ * 3
    jumlah_sks = jumlah * 3
    hasil = total / jumlah_sks
    print(f"IPS Anda semester ini = {hasil:.2f}")

jumlah = int(input("Masukkan jumlah mata kuliah anda = "))
mata_kuliah(jumlah)

