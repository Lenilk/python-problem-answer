k=int(input())
thouson=k//1000
thousonc=k%1000
fivehon=thousonc//500
fivehonc=thousonc%500
houndred=fivehonc//100
houndredc=fivehonc%100
fifty=houndredc//50
fiftyc=houndredc%50
twenty=fiftyc//20
twentyc=fiftyc%20
ten=twentyc//10
tenc=twentyc%10
five=tenc//5
fivec=tenc%5
one=fivec//1
print(thouson)
print(fivehon)
print(houndred)
print(fifty)
print(twenty)
print(ten)
print(five)
print(one)