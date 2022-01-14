class menu:
    def __init__(prog, secim):
        prog.secim = secim
        if secim == "A":
            sayac = 0
            dosya = open("reservation.txt")
            lines = dosya.readlines()[1:]
            dosya.close()
            for line in lines:
                sayac += 1

            if sayac == 0:
                print("Rezervasyon bulunmamaktadır!")
                print()
            else:
                dosya = open("reservation.txt", "r")
                print(dosya.read())
                dosya.close()

        elif secim == "B":
            with open("reservation.txt", "r") as dosya:
                for last_line in dosya:
                    pass

            if last_line[0] == "#":
                num = 1
            else:
                num = int(last_line[0]) + 1

            isim = input("Adınızı giriniz: ")
            tarih = input("Rezervasyon yapacağınız tarihi giriniz: ")
            saat = input("Giriş saatinizi yazın: ")
            yetiskin = int(input("Yetişkin sayısı: "))
            cocuklar = int(input("Çocuk sayısı: "))
            dosya = open("reservation.txt", "a")
            dosya.write(f"{num}\t\t\t{isim}\t\t\t\t{tarih}\t\t\t\t{saat}\t\t\t\t{yetiskin}\t\t\t\t{cocuklar}\n")
            dosya.close()
            print()

        elif secim == "C":
            rezervasyonNumarasi = input("Rezervasyon numaranızı giriniz: ")
            dosya1 = open("reservation.txt", "r")
            lines = dosya1.readlines()
            dosya1.close()
            dosya2 = open("reservation.txt", "w")

            for line in lines:
                if not line.startswith(rezervasyonNumarasi):
                    dosya2.write(line)
            dosya2.close()

        elif secim == "D":
            yetiskin, cocuklar, total_yetiskin, total_cocuklar, toplam = 0, 0, 0, 0, 0
            dosya = open("reservation.txt", "r")
            list_of_lists=[]
            rapor = ""
            i = 0

            for line in dosya:
                i += 1
                if i > 1:

                    stripped_line = line.strip()
                    liste = stripped_line.split("\t\t\t")
                    yetiskin += int(liste[4])
                    cocuklar += int(liste[5])
                    altToplam = (int(liste[4]) * 500) + (int(liste[5]) * 300)
                    toplam += altToplam
                    liste.append(str(altToplam))
                    rapor += f"{liste[0]}\t{liste[2]}\t\t\t{liste[3]}\t\t\t" \
                              f"{liste[1]}\t\t\t{liste[4]}\t\t\t{liste[5]}\t\t\t{liste[6]}\n"
            dosya.close()

            print()
            print()
            print("                                                                       BİLANÇO")
            print()
            print("#\t\t\tTarih\t\t\t\tSaat\t\t\t\tIsim\t\t\t\tYetişkin\t\t\tÇocuklar\t\tAlt Toplam")
            print(rapor)
            print("Yetişkin sayısı: ", yetiskin)
            print("Çocuk sayısı: ", cocuklar)
            print("Toplam ücret: TL ", toplam)
            print("---------------------------------------------------------------- Bizi seçtiğiniz için teşekkür ederiz "
                  "----------------------------------------------------------------")
            print()
            print()

        elif secim == "E":
            import sys
            sys.exit("Bizi seçtiğiniz için teşekkür ederiz!")

        else:
            print("Yanlış tuşladınız. Bir kere daha tekrar edin.")


while True:
    try:
        dosya = open("reservation.txt", "r")
    except FileNotFoundError:
        dosya = open("reservation.txt", "w+")
        dosya.write("#\t\t\tIsim\t\t\t\t\t        Tarih\t\t\t\t\t        Saat\t\t\t    Yetişkin\t\t\tÇocuklar\n")
    dosya.close()

    print("OTEL REZERVASYON SİSTEMİ")
    print("ANA MENÜ:")
    print("A. Bütün rezervasyonları göster\tB. Rezervasyon yaptır")
    print("C. Rezervasyon iptal\t\tD. Bilanço çıkar")
    print("E. Çıkış\n")

    menuSecme = input('Lütfen seçiniz: ').upper()
    menu(menuSecme)
