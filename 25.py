k=int(input())
i=int(input())
if(0<=k<=100 and 100<=i<=200):
    kdif=100-k
    idif=i-100
    if(kdif<idif):
        print(k)
    elif(kdif>idif):
        print(i)
        