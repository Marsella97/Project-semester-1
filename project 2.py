def garis():
    print(50*'-')
#judul
print("================================================================")
print("|\t\t S E L A M A T  D A T A N G                    |")
print("|\t\t D I  G A L A X Y  W A H A N A                 |")
print("================================================================")
nama =input("Masukan Nama Anda         :  ")
usia =int(input("Masukan Usia Anda     : "))
hp   =int(input("Masukan Nomor Telepon : "))
print("================================================================")

#tabel harga
print("_________________________________________________________________")
print("| \tD A F T A R  H A R G A   T I K E T  W A H A N A          |")
print("|________________________________________________________________|")
print("|\t Kode  \t\t Wahana         \t Harga           |")
print("|________________________________________________________________|")
print("|\t KM    \t\t Komedi Putar   \t15.000           |")
print("|\t RH    \t\t Rumah hantu    \t30.000           |")
print("|\t BL    \t\t Bianglala      \t20.000           |")
print("|\t OB    \t\t Ombak Banyu    \t15.000           |")
print("|\t KK    \t\t Kora - Kora    \t25.000           |")
print("|\t MB    \t\t Mandi Bola     \t10.000           |")
print("|\t KG    \t\t Kereta Gantung \t30.000           |")
print("|\t OA    \t\t Ontang-Anting  \t25.000           |")
print("|\t RC    \t\t Roller Coaster \t30.000           |")
print("|________________________________________________________________|")

garis()
Banyak=int(input("Banyaknya wahana yang di pesan: "))
garis()
#skrip 
list_kode =[]
List_jumlah= []
for i in range (Banyak):
    print("\n Pesanan ke-", i+1)
    kode=input("Kode wahana [KM/RH/BL/OB/KK/MB/KG/OA/RC] : ")
    list_kode.append(kode)
    jumlah=int(input("Jumlah Pesan : "))
    List_jumlah.append(jumlah)


#ouput judul
print("\n\n")
print("\t T I K E T  Y A N G  D I  P E S A N")
garis()
print("No  Wahana         Harga      Jumlah    subtotal")
garis()
    
#proses operasi
total_Beli=0

for i in range (Banyak) :
    if list_kode[i]=='KM' or list_kode[i]== 'km':
            wahana = "Komedi Putar"
            harga  = 15000
    elif list_kode[i]=='RH' or list_kode[i]== 'rh' :
            wahana ="Rumah Hantu"
            harga  = 30000
    elif list_kode[i]=='BL' or list_kode[i]== 'bl' :
            wahana ="Bianglala"
            harga  = 20000
    elif list_kode[i]== 'OB' or list_kode[i]== 'ob' :
            wahana ="Ombak Banyu"
            harga  = 15000
    elif list_kode[i]== 'KK' or list_kode[i]== 'kk' :
            wahana = "Kora - Kora"
            harga  = 25000
    elif list_kode[i]== 'MB' or list_kode[i]== "mb" :
            wahana = "Mandi Bola"
            harga  = 10000
    elif list_kode[i]== 'KG' or list_kode[i]== 'kg':
            wahana = "Kereta Gantung"
            harga  = 30000
    elif list_kode[i]== 'OA' or list_kode[i]== 'oa' :
            wahana = "Ontang - Anting"
            harga  = 25000
    elif list_kode[i]== 'RC' or list_kode[i]== 'rc' :
            wahana = "Roller Coaster"
            harga  = 30000
    else :
            wahana ="-"
            harga  = 0
    
    #operasi untuk subtotal
    subtotal = harga * List_jumlah[i]
    #untuk SUM subtotal(menjumlahkan subtotal sesuai dengan perulangan)
    total_Beli=total_Beli + subtotal
    #operasi untuk PPN 5% dari total beli
    ppn = total_Beli* 0.05
    #operasi untuk total bayar dari total_beli + ppn
    total_bayar=total_Beli + ppn

    print(i+1,  wahana ,"\t""Rp." ,harga,"\t""  ",List_jumlah[i], " " ,"\t""Rp.", format(subtotal, ',d').replace(',','.'))
    
garis()
print("\t\t     Total Pembelian    Rp.", format(total_Beli,',d').replace(',','.'))
print("\t\t     Ppn                Rp.", format(round(ppn),',d').replace(',','.'))
print("\t\t     Total Bayar        Rp.", format(round(total_bayar),',d').replace(',','.'))


print ("==========================================================================")
print ("\t\t S E L A M A T  B E R S E N A N G - S E N A N G ")
print ("\t\t          D I  G A L A X Y  W A H A N A")
print("===========================================================================")








