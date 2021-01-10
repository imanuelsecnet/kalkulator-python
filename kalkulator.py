# TOOLS KALKULATOR SEDERHANA BY : FILIPI
import os
import time
os.system("clear")
print ("==================================================")
print ("\t   TOOLS ARITMATIKA BY : IMANUEL    ")
print ("==================================================")
time.sleep(3)
print
time.sleep(2)
print ("1. PENJUMLAHAN")
time.sleep(1)
print ("2. PENGURANGAN")
time.sleep(1)
print ("3. PERKALIAN")
time.sleep(1)
print ("4. PEMBAGIAN")
time.sleep(1)
print ("5. SISA BAGI")
time.sleep(1)
print ("6. PERPANGKATAN")
time.sleep(1)
print
pilih = input ("PILIH MENU : ")

if pilih ==1:
	print
	angka_1 = input ("ANGKA PERTAMA : ")
	angka_2 = input ("ANGKA KEDUA : ")
	total = angka_1 + angka_2
	print
	print "TOTALNYA = ",total
	
elif pilih ==2:
	print
	angka_1 = input ("ANGKA PERTAMA : ")
	angka_2 = input ("ANGKA KEDUA : ")
	total = angka_1 - angka_2
	print
	print "TOTALNYA =", total
	
elif pilih ==3:
	print
	angka_1 = input ("ANGKA PERTAMA : ")
	angka_2 = input ("ANGKA KEDUA : ")
	total = angka_1 * angka_2
	print
	print "TOTALNYA =", total
	
elif pilih ==4:
	print
	angka_1 = input ("ANGKA PERTAMA : ")
	angka_2 = input ("ANGKA KEDUA : ")
	total = angka_1 / angka_2
	print
	print "TOTALNYA = ",total
	
elif pilih ==5:
	print
	angka_1 = input ("ANGKA PERTAMA : ")
	angka_2 = input ("ANGKA KEDUA : ")
	total = angka_1 % angka_2
	print
	print "TOTALNYA = ",total
	
elif pilih ==6:
	print
	angka_1 = input ("ANGKA PERTAMA : ")
	angka_2 = input ("ANGKA KEDUA : ")
	total = angka_1 ** angka_2
	print
	print "TOTALNYA = ",total
	
else:
	print
	print ("MASUKAN INPUT YANG BENAR!!! ")