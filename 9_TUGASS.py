#No 1
def celcius_ke_fahrenheit(celcius):
  return(celcius*1.8+32)

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


#No 2
def is_genap (n):
    return n % 2 == 0
print(is_genap(4))
print(is_genap(7))

#No 3
def nilai(angka = 0):
   if angka >60:
      print("lulus")
   else:
      print("g lulus")
nilai(80)
nilai(60)

#No 4
def bilangan(angka):
   for i in range (1, angka):
      if i % 2 != 0:
         print(i, end=", ")
bilangan(20)