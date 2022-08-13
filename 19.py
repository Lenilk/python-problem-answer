x=float(input())
y=float(input())
z=float(input())
if(0<x<=500 and 0<y<=1000 and 0<z<=x):
    square=x*y
    zsquare=z*z
    dif=square-zsquare
    print("%.2f"%dif)
    if(dif>50):
        print("YES")
    else:
        print("NO")
