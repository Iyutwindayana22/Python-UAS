

def fa():
    print"Modul Nilai Mahasiswa"

 #PROGRAM MENGHITUNG NILAI MAHASISWA
print "\nPOGRAM PYTHON MENGHITUNG NILAI MAHASISWA \n<><><><><><><><><><><><><><><><><><><><>\n"
    
nama=raw_input("Masukkan Nama : ")
uts=input("Masukkan Nilai UTS : ")
uas=input("Masukkan Nilai UAS : ")
tugas=input("Masukkan Nilai Tugas : ")

nilai_uts=uts*40/100;
nilai_uas=uas*40/100;
nilai_tugas=tugas*20/100;
nilai_akhir=nilai_uts+nilai_uas+nilai_tugas;

print "\nNama : ", nama
print "Nilai UTS : %d" %uts
print "Nilai UAS : %d" %uas
print "Nilai Tugas : %d" %tugas
print "Nilai Akhir : " ,float(nilai_akhir);

print "\n NILAI AKHIR MAHASISWA \n..........................\n"

if nilai_akhir >=80 :
    print "\nNilai Huruf : A"
elif nilai_akhir >=70 :
    print "\nNilai Huruf : B"
elif nilai_akhir >=55 :
    print "\nNilai Huruf : C"
elif nilai_akhir >=40 :
    print "\nNilai Huruf : D"
elif nilai_akhir >=39 :
    print "\nNilai Huruf : E"

if nilai_akhir >=60 :
    print "Keterangan : Lulus"
else :
    print "Keterangan : Tidak Lulus"
