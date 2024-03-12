def perkalian(bil1, bil2) :
    hasil_kali = bil1 * bil2
    print(f"{bil1} x {bil2} = ", end = '')
    for i in range(bil1) :
        print(bil2, end = '')
        if i < bil2 :
            print(" + ", end = '')
        else :
            print(f" = {hasil_kali}")

bil1 = int(input("masukkan bilangan pertama = "))
bil2 = int(input("masukkan bilangan kedua = "))
perkalian(bil1, bil2)

