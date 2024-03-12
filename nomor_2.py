def ganjil(bawah, atas) :
    i = 0
    if bawah < atas :
        while bawah <= atas :
            if bawah % 2 == 1 :
                print(bawah, end=' ')
            bawah += 1
    else :
        while atas <= bawah :
            if bawah % 2 == 1 :
                print(bawah, end=' ')
            bawah -= 1

bawah = int(input("Masukkan batas bawah = "))
atas = int(input("Masukkan batas atas = "))

print("Deret bilangan ganjil = ", end = '')
ganjil(bawah, atas)