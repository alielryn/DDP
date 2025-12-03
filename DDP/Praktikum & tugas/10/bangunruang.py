
def kubus (sisi):
    hasil = sisi**3
    return hasil

def balok (p,l,t):
    hasil = p*l*t
    return hasil

def prisma_segitiga (a, ta, t):
    hasil = 0.5*a*ta*t
    return hasil

def tabung (r,t):
    hasil = 3.14*r*r*t
    return hasil

def kerucut (r,t):
    hasil = 1/3*3.14*r**2*t
    return hasil


print(kubus(3))
print(balok(3, 4, 2))
print(prisma_segitiga(3,5,7))
print(tabung(5,10))
print(kerucut(6,10))