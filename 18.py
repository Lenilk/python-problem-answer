x1=float(input())
x2=float(input())
y=float(input())
z=float(input())
if(0<x1<=1000 and 0<x2<=1000 and 0<y<=x2 and 0<z<=x1):
    square=x1*x2
    triangle=(y*z)/2
    dif=square-triangle
    print("%.2f"%dif)
    if(dif>50):
        print("YES")
    else:
        print("NO")