#soru1-tarih yazma
y= int(input("Gun giriniz:"))
a= int(input("Ay giriniz:"))
r= int(input("Yil giriniz:"))
dict_aylar = {1:"Ocak", 2:"Subat", 3:"Mart", 4:"Nisan", 5:"Mayis", 6:"Haziran", 7:"Temmuz", 8:"Agustos", 9:"Eylul", 10:"Ekim", 11:"Kasim", 12:"Aralik"}
yaren = (dict_aylar[a])
print(y,".",yaren,".",r)

#Soru2-fonksiyonu girilen değere göre hesaplama
y = int(input("16'dan kucuk,0'dan buyuk bir sayi giriniz:"))
a = 1
while y> 16 or y< 0:
    y = int(input("Girdiginiz sayi hatalidir. Tekrar sayi giriniz:"))
if 9<= y <16:
    r = 0
    for a in range(y+1):
        e = 2 * a
        r = e + r
        y = y + 1
    print("Girdiğiniz sayi 9 ve 16 arasindadir:", r)
elif 0<= y <9:
    r = 0
    for a in range(y+1):
        e = 3 * a
        r = e + r
        y = y + 1
    print("Girdiginiz sayi 0 ve 9 arasindadir:", r)

#Soru3-Matris kullanarak şifreleme ve çözme
#çözülmesini istediğim şifre = yarenozkanya
#matematikteki şifre sayılarıyla buradaki şifre sayıları tutmuyor hocam bunu düzeltemedim bilginize.
A= [[1,2,-1],
    [2,5,-2],
    [-1,2,2]]

yar= [[25],[1],[18]]

m3= [[0],[0],[0]]
for y in range(len(A)):
    for a in range(len(yar[0])):
        for r in range(len(yar)):
            m3[y][a] +=A[y][r]*yar[r][a]
for R1 in m3:
    print("1.Sifreniz:", R1)

eno= [[5],[14],[15]]
for y in range(len(A)):
    for a in range(len(eno[0])):
        for r in range(len(eno)):
            m3[y][a] +=A[y][r]*eno[r][a]
for R2 in m3:
    print("2.Sifreniz:", R2)

zka= [[26],[11],[1]]
for y in range(len(A)):
    for a in range(len(zka[0])):
        for r in range(len(zka)):
            m3[y][a] +=A[y][r]*zka[r][a]
for R3 in m3:
    print("3.Sifreniz:", R3)

nya= [[14],[25],[1]]
for y in range(len(A)):
    for a in range(len(nya[0])):
        for r in range(len(nya)):
            m3[y][a] +=A[y][r]*nya[r][a]
for R4 in m3:
    print("4.Sifreniz:", R4)

#soru4-asal sayıları bulma
y=[]
for a in range(2,33):
    r = 0
    for e in range(2,a):
        if a%e == 0: r=1
    if r == 0:
        y.append(a)
print(y)