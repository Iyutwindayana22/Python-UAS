def fe():
    print"Modul Dictionary"
    
dict1={'nama1':'Jane doe','nama2':'John Smith','nama3':'Bob Stone','telp1':'+27 555 539','telp2':'+27 555 6254','telp3':'+27 555 5689'}

print 'Name        Telephone Number '
print dict1['nama1'],'   ',dict1['telp1'],'\n',dict1['nama2'],' ',dict1['telp2'],'\n',dict1['nama3'],'  ',dict1['telp3']

dict1['telp1']='+27 555 1024'
print'\nUbah no telp Jane doe'
print 'Name        Telephone Number ' 
print dict1['nama1'],'   ',dict1['telp1'],'\n',dict1['nama2'],' ',dict1['telp2'],'\n',dict1['nama3'],'  ',dict1['telp3']

dict1['nama4']='Anna Cooper'
dict1['telp4']='+27 555 3237'
print'\nMenambah data baru'
print 'Name        Telephone Number '
print dict1['nama1'],'   ',dict1['telp1'],'\n',dict1['nama2'],' ',dict1['telp2'],'\n',dict1['nama3'],'  ',dict1['telp3'],'\n',dict1['nama4'],'',dict1['telp4']



print '\nCetak Nomor Telp Bob stone =',dict1['telp3']

print '\nCetak Semua Key =',dict1.keys()

print '\nCetak semua value =',dict1.values()

