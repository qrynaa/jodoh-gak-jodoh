rimport random
import datetime

print("Pilih metode: ")
print("1. Nama")
print("2. Tanggal")
print("3. Selesai")

ulang = True
while ulang:
    pilihan = input ("Masukkan metode(1/2/3): ")
    
    if pilihan=='1':
        anda = input ("Masukkan nama anda: ")
        pasangan = input ("Masukkan nama pasangan anda: ")
        print("Nama Anda: ", anda)
        print("Nama Pasangan Anda: ", pasangan)

        match = random.randrange(0,100)
        print('kecocokan hubungan anda', match, '%')
        print ("\n","Apakah Mau Mencoba Metode Lain????")
        print ("\n","Tekan Tombol y untuk mencoba metode lain dan n untuk keluar")
        pilih = input("Pilih y or n: ")
        if pilih == "y":
            ulang = True
            print("Pilih metode: ")
            print("1. Nama")
            print("2. Tanggal")
            print("3. Selesai")
        elif pilih == "n":
            ulang = False
    elif pilihan=='2':
        
        print("masukkan data anda")
        n=2
        for i in range(n):
            if i == 1:
                print("masukkan data pasangan anda")
                
            dd = int(input("Masukkan tanggal (dd): "))
            mm = int(input("Masukkan bulan (mm): "))
            yy = int(input("Masukkan tahun (yyyy): "))

            x = datetime.datetime(yy,mm,dd)
            print("Lahir pada: ")
            print(x.strftime("%D"))
            
            
        match1 = random.randrange(100)
        print('kecocokan hubungan anda', match1, '%')

        print ("\n","Apakah Mau Mencoba Metode Lain????")
        print ("\n","Tekan Tombol y untuk mencoba metode lain dan n untuk keluar")
        pilih = input("Pilih y or n: ")
        if pilih == "y":
            ulang = True
            print("Pilih metode: ")
            print("1. Nama")
            print("2. Tanggal")
            print("3. Selesai")
        elif pilih == "n":
            ulang = False
        

    else :
        break;
