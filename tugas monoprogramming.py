#. Nama Anggota Kelompok :
#. 5200411006 - Hamdan Fajril Haqiqie
#. 5200411023 - Adi Wijaya
#. 5200411031 - Riska Dwi Agustin
#. 5200411413 - Juan Fredrick Pandia

print()
print("="*25)
print("Tugas Monoprograming")
print("="*25)

Ram = int(input("\nInput Kapasitas Ram\t: "))
Os  = int(input("Input OS yang digunakan\t: "))

print("RAM\t= ",Ram)
print("OS\t= ",Os)

print("="*25)
pt  = int(input("Input Program terpakai\t: "))
print("="*25)

ptt = Ram - (Os + pt)
print("Program Terpakai\t= ",pt)
print("Program Tidak terpakai\t= ",ptt)