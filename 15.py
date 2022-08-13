n=int(input())
if(0<n<=32767):
    hour=n//3600
    hourc=n%3600
    minute=hourc//60
    minutec=hourc%60
    second=minutec
    print(hour,minute,second)