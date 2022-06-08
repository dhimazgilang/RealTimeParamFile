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

try:
	while True:
		current_files = glob.glob('*')
		if len(current_files) > len(old_files):
			file_baru = beda_anggota(current_files,old_files)
			for file in file_baru:
				print('File baru terdeteksi :',file)
			old_files = current_files[:]
			
		elif len(current_files) < len(old_files):
			file_hilang = beda_anggota(current_files,old_files)
			for file in file_hilang:
				print('File hilang terdeteksi :',file)
			old_files = current_files[:]
		time.sleep(t)
except:
	closing()
