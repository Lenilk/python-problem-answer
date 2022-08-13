k=int(input())
if(10000<=k<=100000):
    total=k*0.93
    print("%.2f"%total)
elif(10000<k):
    print("plese input more price")
else:
    print("plese input less price")