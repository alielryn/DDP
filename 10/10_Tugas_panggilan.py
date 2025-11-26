import bangunruang as br
import bangundatar as bd

print("~~~~~ Bangun Ruang ~~~~~")
print(f"Volume Kubus dengan sisi 3 adalah {br.kubus(4)}")
print(f"Volume balok dengan p=3 l=4 t=2  adalah {br.balok(2,3,6)}")
print(f"Volume prisma segitiga dengan a=3 ta=5 t=7 adalah {br.prisma_segitiga(4,6,4)}")
print(f"Volume tabung dengan r=5 t=10 adalah {br.tabung(4,7)}")
print(f"Volume kerucut dengan r=6 t=10 adalah{br.kerucut(5,7)}")

print("~~~~~ Bangun Datar ~~~~~")
print(f"Luas persegi dengan sisi 4 adalah{bd.persegi(4)}")
print(f"Luas persegi panjang dengan p=7 l=3 adalah {bd.persegi_panjang(7,3)}")
print(f"Luas segitiga dengan a=3 t=5 adalah {bd.segitiga(3,5)}")
print(f"Luas lingkaran dengan r=7 adalah {bd.lingkaran(7)}")
print(f"Luas jajar genjang denga a=6 t= 8 adalah {bd.jajr_genjang(6,8)}")