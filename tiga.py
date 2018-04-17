def fc():
    print"Modul List Append"
i=0
nama=[]
nim=[]
tugas=[]
uts=[]
uas=[]
total=[]

while True:
    s_nama=raw_input('Nama :')
    nama.append(s_nama)
    s_nim=raw_input('NIM :')
    nim.append(s_nim)
    i_tugas=input('Nilai Tugas :')
    tugas.append(i_tugas)
    i_uts=input('Nilai UTS : ')
    uts.append(i_uts)
    i_uas=input('masukan nilai uas :')
    uas.append(i_uas)
    
    rata=(i_tugas+i_uts+i_uas)/3
    total.append(rata)

    lagi=' '
    while lagi!='y' and lagi!='t':
        lagi=raw_input('Tambah Data [y/t] : ')
    i+=1
    if lagi=='t':
        break
print'                                         DAFTAR MAHASISWA'   
print'======================================================================='
print'|No.  |   Nama    |   NIM   |   TUGAS	|  UTS	|  UAS	|   AKHIR   |'
print'======================================================================='
	
for n in range(i):
    print ' ',n+1, '|\t',nama[n],' |',nim[n],' |',tugas[n],' | ',uts[n],' | ',total[n],' |'
	
