# watchdog.py
# script untuk memeriksa apakah ada file baru atau tidak setiap t detik
# untuk menghentikan jalannya script di background windows, 
# ketik tombol berikut bersamaan pada terminal:
# ctrl + C

import glob
import time

import atexit

def beda_anggota(a,b):
    beda = set(a).symmetric_difference(set(b)) 
    return list(beda)
	
def closing():
	print('\n','Selamat Tinggal :)','\n')
	

old_files = glob.glob('*')
t         = 10 # periode pemeriksaan (detik)


print('\n','Halo!','\n')
tulis = []
buat_File = False

try:
	while True:
		current_files = glob.glob('*')
		if len(current_files) > len(old_files):
			buat_File = True
			file_baru = beda_anggota(current_files,old_files)
			for file in file_baru:
				tulis.append('File baru terdeteksi : '+file+'\n')
				print('File baru terdeteksi :',file)
				print('No','\t','RA','\t','DEC','\t','FWHM','\t','count','\t','S/N','\t','mag') 
				for i in range(10):
					tulis.append(str(i+1)+'...'+'\t'+'...'+'\t'+'...'+'\t'+'...'+'\t'+'...'+'\t'+'...\n')
					print(i+1,'\t','...','\t','...','\t','...','\t','...','\t','...','\t','...')
				
				tulis.append('\n')
				print()
				
			old_files = current_files[:]
			
		elif len(current_files) < len(old_files):
			buat_File = True
			file_hilang = beda_anggota(current_files,old_files)
			for file in file_hilang:
				print('File hilang terdeteksi :',file)
				tulis.append('File hilang terdeteksi : '+file+'\n')
			old_files = current_files[:]
		time.sleep(t)
except:
	closing()
	if buat_File == True:
		file_out = open('tabel.dat','w')
		for kalimat in tulis:
			file_out.write(kalimat)
		file_out.close()
