first=float(input())
second=float(input())
third=float(input())
forth=float(input())
fifth=float(input())
all=[first,second,third,forth,fifth]
x=min(all)
ans=all.index(x)
print(ans+1)