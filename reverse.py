n=int(input("Enter Your Input:"))
for i in range(len(str(n))):
    d=n%10
    n=n//10
    print(d,end=" ")
