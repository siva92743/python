n= int(input("enter a num : "))
i=1;j=0
while(i<=n):
    while(j<=i-1):
        print("*",end=" ")
        j+=1
    print("")
    j=0;i+=1

